# Phase 2.4: Mobile App (React Native)

## Overview

**Phase 2.4** extends the platform to mobile devices with a **native React Native application** for iOS and Android, featuring:

- 📱 Native mobile UI (iOS/Android)
- 💬 Real-time chat with push notifications
- 📋 Care plan management
- 📊 Health indicator tracking
- 🔐 Biometric authentication
- 📴 Offline-first architecture
- 🔄 Automatic sync when online

**Prerequisites:**
- Phase 2.1 (PostgreSQL Database)
- Phase 2.2 (Analytics)
- Phase 2.3 (FHIR Integration) - optional

---

## Architecture

```
┌─────────────────────────────────────────┐
│    iOS App (Swift/Objective-C)         │
├─────────────────────────────────────────┤
│    React Native Bridge                  │
├─────────────────────────────────────────┤
│    JavaScript/TypeScript Layer          │
│  (App.tsx, screens, components)         │
├─────────────────────────────────────────┤
│    Redux State Management               │
│  (Store, reducers, actions)             │
├─────────────────────────────────────────┤
│    API Client & Sync Engine             │
├─────────────────────────────────────────┤
│    Local Storage (SQLite/AsyncStorage)  │
├─────────────────────────────────────────┤
│    Backend APIs                         │
│  (app.py, app_phase2.py)               │
├─────────────────────────────────────────┤
│    PostgreSQL Database                  │
└─────────────────────────────────────────┘
```

---

## Setup Instructions

### 1. Environment Setup

```bash
# Install Node.js and npm (if not already installed)
node --version  # Should be 18+
npm --version   # Should be 8+

# Install React Native CLI
npm install -g react-native-cli

# Install iOS/Android requirements
# macOS: Install Xcode and CocoaPods
xcode-select --install
sudo gem install cocoapods

# Android: Install Android Studio
# https://developer.android.com/studio
```

### 2. Create Mobile Project

```bash
# Navigate to mobile directory
cd mobile

# Install dependencies
npm install

# Install Pods (iOS)
cd ios && pod install && cd ..
```

### 3. Configure Backend Connection

```bash
# Create .env file
cat > .env << 'EOF'
REACT_APP_API_URL=https://your-backend.com
REACT_APP_API_TIMEOUT=10000
REACT_APP_FIREBASE_API_KEY=your_firebase_key
REACT_APP_FIREBASE_PROJECT_ID=your_project_id
REACT_APP_ENABLE_OFFLINE=true
REACT_APP_ENABLE_PUSH_NOTIFICATIONS=true
EOF
```

### 4. Run on Simulator/Device

```bash
# iOS Simulator
npm run ios
# or
react-native run-ios

# Android Emulator
npm run android
# or
react-native run-android

# Device (iOS)
react-native run-ios --device "Device Name"

# Device (Android)
react-native run-android
```

---

## Core Features

### 1. **Authentication**

```typescript
// Login with credentials
import { authService } from './services/authService';

const login = async (username: string, password: string) => {
  try {
    const response = await authService.login(username, password);
    await AsyncStorage.setItem('authToken', response.token);
    dispatch(setAuth(response.user));
  } catch (error) {
    console.error('Login failed:', error);
  }
};

// Biometric login (iOS/Android)
import * as LocalAuthentication from 'react-native-local-authentication';

const biometricLogin = async () => {
  try {
    const compatible = await LocalAuthentication.hasHardwareAsync();
    if (compatible) {
      await LocalAuthentication.authenticateAsync({
        disableDeviceFallback: false,
      });
      // Load token from secure storage
    }
  } catch (error) {
    console.error('Biometric auth failed:', error);
  }
};
```

### 2. **Real-time Chat**

```typescript
// Send message
import { chatService } from './services/chatService';

const sendMessage = async (text: string) => {
  try {
    const message = {
      id: Date.now(),
      text,
      sender: 'user',
      timestamp: new Date(),
      synced: false,
    };
    
    // Save locally first
    dispatch(addMessage(message));
    
    // Sync when online
    if (isOnline) {
      const response = await chatService.sendMessage(text);
      dispatch(updateMessage({ id: message.id, ...response }));
    }
  } catch (error) {
    console.error('Message send failed:', error);
  }
};

// Listen for push notifications
messaging().onMessage(async (remoteMessage) => {
  console.log('Notification received:', remoteMessage);
  dispatch(addNotification(remoteMessage));
});
```

### 3. **Offline-First Sync**

```typescript
// Redux Persist for offline support
import { persistStore, persistReducer } from 'redux-persist';
import AsyncStorage from '@react-native-async-storage/async-storage';

const persistConfig = {
  key: 'root',
  storage: AsyncStorage,
  whitelist: ['chat', 'user', 'patients'],
};

const persistedReducer = persistReducer(persistConfig, rootReducer);

// Sync when connection restored
NetInfo.addEventListener(state => {
  if (state.isConnected && hasPendingChanges) {
    syncWithServer();
  }
});
```

### 4. **Care Plan Management**

```typescript
// View patient care plans
import { carePlanService } from './services/carePlanService';

const loadCarePlans = async (patientId: string) => {
  try {
    let plans = await AsyncStorage.getItem(`carePlans_${patientId}`);
    
    if (!plans || isStale(plans)) {
      plans = await carePlanService.getCarePlans(patientId);
      await AsyncStorage.setItem(
        `carePlans_${patientId}`,
        JSON.stringify(plans)
      );
    }
    
    dispatch(setCarePlans(JSON.parse(plans)));
  } catch (error) {
    console.error('Load care plans failed:', error);
  }
};
```

### 5. **Health Indicators**

```typescript
// Track vital signs
import { healthService } from './services/healthService';

const recordVitals = async (vitals: VitalsData) => {
  try {
    const observation = {
      bloodPressure: vitals.bp,
      temperature: vitals.temp,
      oxygenSaturation: vitals.o2,
      heartRate: vitals.hr,
      recordedAt: new Date(),
      synced: false,
    };
    
    // Save locally
    await AsyncStorage.setItem(
      'lastVitals',
      JSON.stringify(observation)
    );
    
    // Sync to server
    if (isOnline) {
      await healthService.recordObservation(observation);
    }
  } catch (error) {
    console.error('Record vitals failed:', error);
  }
};
```

---

## Project Structure

```
mobile/
├── App.tsx                          # Main app entry
├── package.json                     # Dependencies
├── tsconfig.json                    # TypeScript config
├── babel.config.js                  # Babel config
├── app.json                         # App metadata
├── index.js                         # React Native entry
│
├── src/
│   ├── screens/
│   │   ├── LoginScreen.tsx          # Authentication
│   │   ├── ChatScreen.tsx           # Chat interface
│   │   ├── CarePlanScreen.tsx       # Care plan view
│   │   ├── ProblemsScreen.tsx       # Problems/diagnoses
│   │   ├── InterventionsScreen.tsx  # Interventions
│   │   ├── HealthIndicatorsScreen.tsx
│   │   ├── SettingsScreen.tsx       # User settings
│   │   └── PatientDetailsScreen.tsx # Patient info
│   │
│   ├── components/
│   │   ├── ChatBubble.tsx           # Message component
│   │   ├── CarePlanCard.tsx         # Care plan card
│   │   ├── HealthIndicator.tsx      # Vital signs
│   │   ├── LoadingSpinner.tsx       # Loading UI
│   │   └── ErrorBoundary.tsx        # Error handling
│   │
│   ├── services/
│   │   ├── authService.ts           # Authentication
│   │   ├── chatService.ts           # Chat API
│   │   ├── carePlanService.ts       # Care plans
│   │   ├── healthService.ts         # Health data
│   │   ├── syncService.ts           # Offline sync
│   │   └── api.ts                   # HTTP client
│   │
│   ├── store/
│   │   ├── index.ts                 # Store setup
│   │   ├── rootReducer.ts           # Root reducer
│   │   ├── slices/
│   │   │   ├── authSlice.ts         # Auth state
│   │   │   ├── chatSlice.ts         # Chat state
│   │   │   ├── patientSlice.ts      # Patient state
│   │   │   └── uiSlice.ts           # UI state
│   │   └── hooks.ts                 # Redux hooks
│   │
│   ├── types/
│   │   ├── index.ts                 # TypeScript types
│   │   ├── auth.ts                  # Auth types
│   │   ├── chat.ts                  # Chat types
│   │   └── patient.ts               # Patient types
│   │
│   ├── utils/
│   │   ├── formatters.ts            # Data formatting
│   │   ├── validators.ts            # Input validation
│   │   ├── storage.ts               # Local storage
│   │   └── networkStatus.ts         # Network detection
│   │
│   ├── styles/
│   │   ├── colors.ts                # Theme colors
│   │   ├── fonts.ts                 # Typography
│   │   └── spacing.ts               # Spacing scale
│   │
│   └── config/
│       ├── constants.ts             # App constants
│       ├── environment.ts           # Env vars
│       └── logger.ts                # Logging
│
├── ios/                             # iOS native code
│   ├── Podfile                      # iOS dependencies
│   └── NursingValidator/            # iOS app files
│
├── android/                         # Android native code
│   ├── build.gradle                 # Android config
│   └── app/                         # Android app files
│
└── __tests__/
    ├── screens/                     # Screen tests
    ├── components/                  # Component tests
    ├── services/                    # Service tests
    └── store/                       # Redux tests
```

---

## Key Packages

### Navigation
- `@react-navigation/native` - Navigation framework
- `@react-navigation/bottom-tabs` - Tab navigator
- `@react-navigation/stack` - Stack navigator

### State Management
- `redux` - State container
- `@reduxjs/toolkit` - Redux utilities
- `redux-persist` - Persist state

### UI Components
- `react-native-vector-icons` - Icons
- `react-native-svg` - SVG support
- `react-native-gesture-handler` - Gestures

### Firebase
- `@react-native-firebase/app` - Firebase core
- `@react-native-firebase/messaging` - Push notifications
- `@react-native-firebase/analytics` - Analytics

### Storage
- `@react-native-async-storage/async-storage` - Key-value storage
- `react-native-sqlite-storage` - Local database

### Forms
- `formik` - Form management
- `yup` - Validation schema

---

## Push Notifications Setup

### Firebase Cloud Messaging (FCM)

```bash
# 1. Create Firebase project
# https://firebase.google.com/

# 2. Download google-services.json (Android)
# Place in: android/app/google-services.json

# 3. Download GoogleService-Info.plist (iOS)
# Place in: ios/GoogleService-Info.plist

# 4. Install React Native Firebase
npm install @react-native-firebase/app @react-native-firebase/messaging

# 5. Link native modules
cd ios && pod install && cd ..
```

### Push Notification Handler

```typescript
import messaging from '@react-native-firebase/messaging';

// Handle foreground messages
messaging().onMessage(async (remoteMessage) => {
  console.log('Foreground message:', remoteMessage);
  // Update UI with notification
});

// Handle background/killed messages
messaging().onNotificationOpenedApp((remoteMessage) => {
  console.log('App opened from notification:', remoteMessage);
  // Navigate to appropriate screen
});

// Get initial notification (app closed)
messaging()
  .getInitialNotification()
  .then((remoteMessage) => {
    if (remoteMessage) {
      console.log('App opened from quit state:', remoteMessage);
    }
  });
```

---

## Testing

### Unit Tests

```bash
# Run tests
npm test

# With coverage
npm test -- --coverage
```

### E2E Tests

```bash
# Detox setup
npm install -g detox-cli
detox build-framework-cache

# Run E2E tests
detox test e2e --configuration ios.sim.debug
```

### Sample Test

```typescript
import { render, screen, fireEvent } from '@testing-library/react-native';
import LoginScreen from '../screens/LoginScreen';

describe('LoginScreen', () => {
  it('renders login form', () => {
    render(<LoginScreen />);
    expect(screen.getByPlaceholderText('Username')).toBeTruthy();
  });

  it('submits login form', async () => {
    const { getByPlaceholderText, getByText } = render(<LoginScreen />);
    
    fireEvent.changeText(getByPlaceholderText('Username'), 'nurse');
    fireEvent.changeText(getByPlaceholderText('Password'), 'nurse2025');
    fireEvent.press(getByText('Login'));
    
    // Assert navigation or API call
  });
});
```

---

## Troubleshooting

### Build Errors

```bash
# Clear cache and rebuild
rm -rf node_modules
rm -rf Pods
npm install
cd ios && pod install && cd ..
npm run ios
```

### Simulator Issues

```bash
# Reset simulator
xcrun simctl erase all

# Rebuild and run
npm run ios
```

### Android Issues

```bash
# Clear Gradle cache
cd android && ./gradlew clean && cd ..

# Rebuild
npm run android
```

---

## Backend API Integration

### API Endpoints Required

```
POST   /api/v1/auth/login           - User authentication
POST   /api/v1/auth/logout          - User logout
GET    /api/v1/user/profile         - Get user profile
POST   /api/v1/chat/send            - Send message
GET    /api/v1/chat/history         - Get messages
GET    /api/v1/patients             - List patients
GET    /api/v1/patients/{id}        - Get patient
GET    /api/v1/patients/{id}/plans  - Get care plans
GET    /api/v1/health/vitals        - Get vital signs
POST   /api/v1/health/vitals        - Record vitals
POST   /api/v1/notifications/token  - Register push token
```

### API Client Example

```typescript
// src/services/api.ts
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL,
  timeout: 10000,
});

// Add auth token to requests
api.interceptors.request.use(async (config) => {
  const token = await AsyncStorage.getItem('authToken');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle token expiry
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      // Token expired, redirect to login
      await AsyncStorage.removeItem('authToken');
      // Navigation.navigate('Login');
    }
    return Promise.reject(error);
  }
);

export default api;
```

---

## Performance Optimization

### Image Optimization

```typescript
import FastImage from 'react-native-fast-image';

// Use FastImage instead of Image
<FastImage
  source={{ uri: imageUrl, priority: FastImage.priority.normal }}
  style={{ width: 200, height: 200 }}
  resizeMode={FastImage.resizeMode.contain}
/>
```

### FlatList Performance

```typescript
// Optimize list rendering
<FlatList
  data={messages}
  renderItem={({ item }) => <ChatBubble {...item} />}
  keyExtractor={(item) => item.id}
  removeClippedSubviews={true}
  maxToRenderPerBatch={10}
  updateCellsBatchingPeriod={50}
  initialNumToRender={10}
  onEndReachedThreshold={0.5}
  onEndReached={loadMoreMessages}
/>
```

### Code Splitting

```typescript
// Lazy load screens
const CarePlanScreen = React.lazy(() => import('./CarePlanScreen'));
const ProblemsScreen = React.lazy(() => import('./ProblemsScreen'));
```

---

## Deployment

### iOS App Store

```bash
# Build release
npm run build:ios

# Submit to App Store Connect
# https://appstoreconnect.apple.com
```

### Google Play Store

```bash
# Build release APK
npm run build:android

# Upload to Google Play Console
# https://play.google.com/console
```

---

## Next Steps

1. Set up development environment (Node.js, Xcode, Android Studio)
2. Clone mobile project
3. Configure backend connection
4. Run on simulator/device
5. Implement push notifications
6. Add biometric authentication
7. Test offline sync
8. Deploy to app stores

---

## Files Provided

**New Files:**
- `mobile/package.json` - Dependencies
- `mobile/App.tsx` - Main app component
- `mobile/src/screens/` - Screen components (skeleton)
- `mobile/src/services/` - API services (skeleton)
- `mobile/src/store/` - Redux state (skeleton)

**Documentation:**
- `PHASE2_MOBILE.md` (this file)

---

## References

- [React Native Docs](https://reactnative.dev/)
- [React Navigation](https://reactnavigation.org/)
- [Redux Toolkit](https://redux-toolkit.js.org/)
- [Firebase React Native](https://rnfirebase.io/)
- [React Native Firebase Messaging](https://rnfirebase.io/messaging/overview)

---

*Phase 2.4 Mobile App - November 29, 2025*
