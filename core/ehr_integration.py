"""
Phase 2.3: EHR/FHIR Integration Module

Provides FHIR-compliant APIs, HL7 messaging support, and real patient data
integration with Electronic Health Record systems.
"""

import json
import logging
from datetime import datetime
from typing import Optional, Dict, Any, List
from enum import Enum

try:
    from fhir.resources.R4B.bundle import Bundle
    from fhir.resources.R4B.bundle import BundleEntry
    from fhir.resources.R4B.patient import Patient
    from fhir.resources.R4B.condition import Condition
    from fhir.resources.R4B.observation import Observation
    from fhir.resources.R4B.goal import Goal
    from fhir.resources.R4B.careplan import CarePlan

    FHIR_AVAILABLE = True
except ImportError:
    FHIR_AVAILABLE = False

logger = logging.getLogger(__name__)


class FHIRResourceType(str, Enum):
    """FHIR Resource Types supported by the system."""

    PATIENT = "Patient"
    CONDITION = "Condition"
    OBSERVATION = "Observation"
    GOAL = "Goal"
    CARE_PLAN = "CarePlan"
    MEDICATION = "Medication"
    PROCEDURE = "Procedure"
    APPOINTMENT = "Appointment"
    BUNDLE = "Bundle"


class FHIRAPIClient:
    """FHIR API Client for interacting with EHR systems."""

    def __init__(self, base_url: str, api_key: Optional[str] = None):
        """
        Initialize FHIR API client.

        Args:
            base_url: FHIR server base URL (e.g., https://fhir.example.com)
            api_key: Optional API key for authentication
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/fhir+json",
            "Accept": "application/fhir+json",
        }
        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"

        logger.info(f"FHIR API client initialized for {base_url}")

    def get_patient(self, patient_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve a patient resource from the FHIR server.

        Args:
            patient_id: FHIR patient ID

        Returns:
            Patient resource as dictionary
        """
        try:
            import requests

            url = f"{self.base_url}/Patient/{patient_id}"
            response = requests.get(url, headers=self.headers, timeout=10)

            if response.status_code == 200:
                logger.info(f"Retrieved patient: {patient_id}")
                return response.json()
            else:
                logger.warning(
                    f"Failed to retrieve patient {patient_id}: "
                    f"{response.status_code}"
                )
                return None
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Error retrieving patient", e)
            return None

    def get_patient_conditions(self, patient_id: str) -> List[Dict[str, Any]]:
        """
        Retrieve all conditions for a patient.

        Args:
            patient_id: FHIR patient ID

        Returns:
            List of Condition resources
        """
        try:
            import requests

            url = f"{self.base_url}/Condition?subject=Patient/{patient_id}"
            response = requests.get(url, headers=self.headers, timeout=10)

            if response.status_code == 200:
                bundle = response.json()
                entries = bundle.get("entry", [])
                conditions = [entry["resource"] for entry in entries]
                logger.info(
                    f"Retrieved {len(conditions)} conditions for patient "
                    f"{patient_id}"
                )
                return conditions
            else:
                logger.warning(
                    f"Failed to retrieve conditions for patient {patient_id}: "
                    f"{response.status_code}"
                )
                return []
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Error retrieving conditions", e)
            return []

    def get_patient_observations(
        self, patient_id: str, observation_type: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Retrieve observations (vital signs, labs) for a patient.

        Args:
            patient_id: FHIR patient ID
            observation_type: Optional filter by code

        Returns:
            List of Observation resources
        """
        try:
            import requests

            query = f"subject=Patient/{patient_id}"
            if observation_type:
                query += f"&code={observation_type}"

            url = f"{self.base_url}/Observation?{query}"
            response = requests.get(url, headers=self.headers, timeout=10)

            if response.status_code == 200:
                bundle = response.json()
                entries = bundle.get("entry", [])
                observations = [entry["resource"] for entry in entries]
                logger.info(
                    f"Retrieved {len(observations)} observations for patient "
                    f"{patient_id}"
                )
                return observations
            else:
                logger.warning(
                    f"Failed to retrieve observations: {response.status_code}"
                )
                return []
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Error retrieving observations", e)
            return []

    def get_patient_care_plans(self, patient_id: str) -> List[Dict[str, Any]]:
        """
        Retrieve care plans for a patient.

        Args:
            patient_id: FHIR patient ID

        Returns:
            List of CarePlan resources
        """
        try:
            import requests

            url = f"{self.base_url}/CarePlan?subject=Patient/{patient_id}"
            response = requests.get(url, headers=self.headers, timeout=10)

            if response.status_code == 200:
                bundle = response.json()
                entries = bundle.get("entry", [])
                care_plans = [entry["resource"] for entry in entries]
                logger.info(
                    f"Retrieved {len(care_plans)} care plans for patient "
                    f"{patient_id}"
                )
                return care_plans
            else:
                logger.warning(
                    f"Failed to retrieve care plans: {response.status_code}"
                )
                return []
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Error retrieving care plans", e)
            return []

    def get_patient_goals(self, patient_id: str) -> List[Dict[str, Any]]:
        """
        Retrieve goals for a patient.

        Args:
            patient_id: FHIR patient ID

        Returns:
            List of Goal resources
        """
        try:
            import requests

            url = f"{self.base_url}/Goal?subject=Patient/{patient_id}"
            response = requests.get(url, headers=self.headers, timeout=10)

            if response.status_code == 200:
                bundle = response.json()
                entries = bundle.get("entry", [])
                goals = [entry["resource"] for entry in entries]
                logger.info(
                    f"Retrieved {len(goals)} goals for patient {patient_id}"
                )
                return goals
            else:
                logger.warning(f"Failed to retrieve goals: {response.status_code}")
                return []
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Error retrieving goals", e)
            return []

    def create_observation(self, patient_id: str, data: Dict[str, Any]) -> Optional[str]:
        """
        Create a new observation for a patient.

        Args:
            patient_id: FHIR patient ID
            data: Observation data

        Returns:
            New resource ID or None on failure
        """
        try:
            import requests

            observation = {
                "resourceType": "Observation",
                "status": "final",
                "subject": {"reference": f"Patient/{patient_id}"},
                "effectiveDateTime": datetime.utcnow().isoformat(),
                **data,
            }

            url = f"{self.base_url}/Observation"
            response = requests.post(
                url, json=observation, headers=self.headers, timeout=10
            )

            if response.status_code in [200, 201]:
                new_id = response.headers.get(
                    "Location", ""
                ).split("/")[-1]
                logger.info(
                    f"Created observation for patient {patient_id}: {new_id}"
                )
                return new_id
            else:
                logger.warning(
                    f"Failed to create observation: {response.status_code}"
                )
                return None
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Error creating observation", e)
            return None

    def update_care_plan(
        self, care_plan_id: str, data: Dict[str, Any]
    ) -> bool:
        """
        Update a care plan.

        Args:
            care_plan_id: FHIR CarePlan ID
            data: Updated data

        Returns:
            True on success, False otherwise
        """
        try:
            import requests

            url = f"{self.base_url}/CarePlan/{care_plan_id}"
            response = requests.put(
                url, json=data, headers=self.headers, timeout=10
            )

            if response.status_code in [200, 204]:
                logger.info(f"Updated care plan: {care_plan_id}")
                return True
            else:
                logger.warning(
                    f"Failed to update care plan: {response.status_code}"
                )
                return False
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Error updating care plan", e)
            return False


class HL7Parser:
    """HL7 v2 message parser for EHR interoperability."""

    @staticmethod
    def parse_hl7_message(message: str) -> Dict[str, Any]:
        """
        Parse HL7 v2 message into structured data.

        Args:
            message: HL7 v2 message string

        Returns:
            Parsed message as dictionary
        """
        try:
            lines = message.strip().split("\r")
            parsed = {}

            for line in lines:
                segments = line.split("|")
                segment_type = segments[0]

                if segment_type == "PID":
                    parsed["patient"] = {
                        "id": segments[3],
                        "name": segments[5],
                        "dob": segments[7],
                        "gender": segments[8],
                    }
                elif segment_type == "OBX":
                    if "observations" not in parsed:
                        parsed["observations"] = []
                    parsed["observations"].append(
                        {
                            "type": segments[2],
                            "value": segments[5],
                            "units": segments[6],
                        }
                    )
                elif segment_type == "ORC":
                    parsed["order"] = {
                        "control_id": segments[1],
                        "status": segments[2],
                    }

            logger.info("Parsed HL7 message successfully")
            return parsed
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Error parsing HL7 message", e)
            return {}

    @staticmethod
    def create_hl7_message(
        message_type: str, data: Dict[str, Any]
    ) -> str:
        """
        Create an HL7 v2 message.

        Args:
            message_type: Type of message (e.g., ADT, ORM)
            data: Message data

        Returns:
            HL7 v2 formatted message
        """
        try:
            segments = []

            # MSH segment (header)
            segments.append(f"MSH|^~\\&|{data.get('sending_app', 'APP')}|"
                          f"{data.get('sending_facility', 'FAC')}|"
                          f"{data.get('receiving_app', 'APP')}|"
                          f"{data.get('receiving_facility', 'FAC')}|"
                          f"{datetime.utcnow().isoformat()}|||")

            # PID segment (patient)
            if "patient" in data:
                segments.append(
                    f"PID|||{data['patient'].get('id', '')}||"
                    f"{data['patient'].get('name', '')}||"
                    f"{data['patient'].get('dob', '')}|"
                    f"{data['patient'].get('gender', '')}"
                )

            message = "\r".join(segments)
            logger.info(f"Created HL7 {message_type} message")
            return message
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Error creating HL7 message", e)
            return ""


class FHIRResourceBuilder:
    """Builder for creating FHIR resources."""

    @staticmethod
    def build_condition(
        patient_id: str,
        code: str,
        display: str,
        onset_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Build a FHIR Condition resource.

        Args:
            patient_id: Patient ID
            code: Condition code (SNOMED/ICD)
            display: Condition display name
            onset_date: Date condition started

        Returns:
            FHIR Condition resource
        """
        return {
            "resourceType": "Condition",
            "subject": {"reference": f"Patient/{patient_id}"},
            "code": {"coding": [{"code": code, "display": display}]},
            "onsetDateTime": onset_date or datetime.utcnow().isoformat(),
            "recordedDate": datetime.utcnow().isoformat(),
        }

    @staticmethod
    def build_observation(
        patient_id: str,
        code: str,
        value: float,
        unit: str,
        reference_range: Optional[tuple] = None,
    ) -> Dict[str, Any]:
        """
        Build a FHIR Observation resource.

        Args:
            patient_id: Patient ID
            code: Observation code
            value: Measured value
            unit: Unit of measurement
            reference_range: Optional (low, high) tuple

        Returns:
            FHIR Observation resource
        """
        obs = {
            "resourceType": "Observation",
            "status": "final",
            "subject": {"reference": f"Patient/{patient_id}"},
            "code": {"coding": [{"code": code}]},
            "valueQuantity": {"value": value, "unit": unit},
            "effectiveDateTime": datetime.utcnow().isoformat(),
        }

        if reference_range:
            obs["referenceRange"] = [
                {
                    "low": {"value": reference_range[0]},
                    "high": {"value": reference_range[1]},
                }
            ]

        return obs

    @staticmethod
    def build_goal(
        patient_id: str,
        description: str,
        status: str = "proposed",
        target_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Build a FHIR Goal resource.

        Args:
            patient_id: Patient ID
            description: Goal description
            status: Goal status (proposed, accepted, in-progress, achieved, etc.)
            target_date: Target date for achievement

        Returns:
            FHIR Goal resource
        """
        return {
            "resourceType": "Goal",
            "subject": {"reference": f"Patient/{patient_id}"},
            "description": {
                "text": description,
            },
            "status": status,
            "targetDate": target_date or datetime.utcnow().isoformat(),
        }


class EHRIntegrationManager:
    """Manager for EHR system integration."""

    def __init__(self, fhir_url: str, api_key: Optional[str] = None):
        """Initialize EHR integration."""
        self.fhir_client = FHIRAPIClient(fhir_url, api_key)
        self.hl7_parser = HL7Parser()
        self.resource_builder = FHIRResourceBuilder()
        logger.info("EHR Integration Manager initialized")

    def sync_patient_data(self, patient_id: str) -> Dict[str, Any]:
        """
        Sync all patient data from EHR system.

        Args:
            patient_id: Patient ID

        Returns:
            Complete patient record
        """
        try:
            patient_data = {
                "patient": self.fhir_client.get_patient(patient_id),
                "conditions": self.fhir_client.get_patient_conditions(patient_id),
                "observations": self.fhir_client.get_patient_observations(
                    patient_id
                ),
                "care_plans": self.fhir_client.get_patient_care_plans(
                    patient_id
                ),
                "goals": self.fhir_client.get_patient_goals(patient_id),
            }
            logger.info("Synced patient data successfully")
            return patient_data
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Error syncing patient data", e)
            return {}

    def send_observation_to_ehr(
        self, patient_id: str, observation: Dict[str, Any]
    ) -> Optional[str]:
        """
        Send observation data to EHR system.

        Args:
            patient_id: Patient ID
            observation: Observation data

        Returns:
            Observation ID or None
        """
        try:
            obs_id = self.fhir_client.create_observation(
                patient_id, observation
            )
            logger.info(f"Sent observation to EHR: {obs_id}")
            return obs_id
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Error sending observation", e)
            return None

    def process_hl7_message(self, message: str) -> Dict[str, Any]:
        """
        Process incoming HL7 message from EHR.

        Args:
            message: HL7 v2 message

        Returns:
            Parsed message data
        """
        try:
            parsed = self.hl7_parser.parse_hl7_message(message)
            logger.info("Processed HL7 message successfully")
            return parsed
        except Exception as e:
            from core.safe_logging import log_exception_safe
            log_exception_safe(logger, "Error processing HL7 message", e)
            return {}
