/**
 * Phase 2.4: Mobile App - Main Application Component
 * 
 * NHS Unified Nursing Validator Mobile Application
 * React Native with TypeScript
 */

import React, { useEffect } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { Provider } from 'react-redux';
import { PersistGate } from 'redux-persist/integration/react';
import store, { persistor } from './store';
import AsyncStorage from '@react-native-async-storage/async-storage';
import messaging from '@react-native-firebase/messaging';
import Icon from 'react-native-vector-icons/MaterialIcons';

// Navigation
const Stack = createNativeStackNavigator();
const Tab = createBottomTabNavigator();

// Screens
import LoginScreen from './screens/LoginScreen';
import ChatScreen from './screens/ChatScreen';
import CarePlanScreen from './screens/CarePlanScreen';
import ProblemsScreen from './screens/ProblemsScreen';
import InterventionsScreen from './screens/InterventionsScreen';
import HealthIndicatorsScreen from './screens/HealthIndicatorsScreen';
import SettingsScreen from './screens/SettingsScreen';
import PatientDetailsScreen from './screens/PatientDetailsScreen';

/**
 * Chat Tab Navigator
 */
const ChatTab = () => {
  return (
    <Stack.Navigator
      screenOptions={{
        headerShown: true,
        headerTintColor: '#1f77b4',
      }}
    >
      <Stack.Screen
        name="ChatHome"
        component={ChatScreen}
        options={{
          title: 'Clinical Assistant',
          headerTintColor: '#1f77b4',
        }}
      />
    </Stack.Navigator>
  );
};

/**
 * Care Plan Tab Navigator
 */
const CarePlanTab = () => {
  return (
    <Stack.Navigator
      screenOptions={{
        headerShown: true,
      }}
    >
      <Stack.Screen
        name="CarePlanHome"
        component={CarePlanScreen}
        options={{
          title: 'Care Plans',
        }}
      />
      <Stack.Screen
        name="PatientDetails"
        component={PatientDetailsScreen}
        options={{
          title: 'Patient Details',
        }}
      />
    </Stack.Navigator>
  );
};

/**
 * Problems Tab Navigator
 */
const ProblemsTab = () => {
  return (
    <Stack.Navigator
      screenOptions={{
        headerShown: true,
      }}
    >
      <Stack.Screen
        name="ProblemsHome"
        component={ProblemsScreen}
        options={{
          title: 'Problems',
        }}
      />
    </Stack.Navigator>
  );
};

/**
 * Interventions Tab Navigator
 */
const InterventionsTab = () => {
  return (
    <Stack.Navigator
      screenOptions={{
        headerShown: true,
      }}
    >
      <Stack.Screen
        name="InterventionsHome"
        component={InterventionsScreen}
        options={{
          title: 'Interventions',
        }}
      />
    </Stack.Navigator>
  );
};

/**
 * Health Tab Navigator
 */
const HealthTab = () => {
  return (
    <Stack.Navigator
      screenOptions={{
        headerShown: true,
      }}
    >
      <Stack.Screen
        name="HealthHome"
        component={HealthIndicatorsScreen}
        options={{
          title: 'Health Indicators',
        }}
      />
    </Stack.Navigator>
  );
};

/**
 * Settings Tab Navigator
 */
const SettingsTab = () => {
  return (
    <Stack.Navigator
      screenOptions={{
        headerShown: true,
      }}
    >
      <Stack.Screen
        name="SettingsHome"
        component={SettingsScreen}
        options={{
          title: 'Settings',
        }}
      />
    </Stack.Navigator>
  );
};

/**
 * Main Tab Navigator (Authenticated)
 */
const MainTabNavigator = () => {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        headerShown: false,
        tabBarIcon: ({ focused, color, size }) => {
          let iconName;
          const iconSize = 24;

          switch (route.name) {
            case 'Chat':
              iconName = focused ? 'chat-bubble' : 'chat-bubble-outline';
              break;
            case 'CarePlan':
              iconName = focused ? 'assignment' : 'assignment-outlined';
              break;
            case 'Problems':
              iconName = focused ? 'warning' : 'warning-outlined';
              break;
            case 'Interventions':
              iconName = focused ? 'local-hospital' : 'local-hospital';
              break;
            case 'Health':
              iconName = focused ? 'favorite' : 'favorite-outline';
              break;
            case 'Settings':
              iconName = focused ? 'settings' : 'settings-outline';
              break;
            default:
              iconName = 'home';
          }

          return <Icon name={iconName} size={iconSize} color={color} />;
        },
        tabBarActiveTintColor: '#1f77b4',
        tabBarInactiveTintColor: '#999',
      })}
    >
      <Tab.Screen
        name="Chat"
        component={ChatTab}
        options={{
          title: 'Chat',
          tabBarLabel: 'Chat',
        }}
      />
      <Tab.Screen
        name="CarePlan"
        component={CarePlanTab}
        options={{
          title: 'Care Plans',
          tabBarLabel: 'Plans',
        }}
      />
      <Tab.Screen
        name="Problems"
        component={ProblemsTab}
        options={{
          title: 'Problems',
          tabBarLabel: 'Problems',
        }}
      />
      <Tab.Screen
        name="Interventions"
        component={InterventionsTab}
        options={{
          title: 'Interventions',
          tabBarLabel: 'Actions',
        }}
      />
      <Tab.Screen
        name="Health"
        component={HealthTab}
        options={{
          title: 'Health',
          tabBarLabel: 'Health',
        }}
      />
      <Tab.Screen
        name="Settings"
        component={SettingsTab}
        options={{
          title: 'Settings',
          tabBarLabel: 'More',
        }}
      />
    </Tab.Navigator>
  );
};

/**
 * Root Navigator
 */
const RootNavigator = ({ isAuthenticated }) => {
  return (
    <NavigationContainer>
      <Stack.Navigator
        screenOptions={{
          headerShown: false,
        }}
      >
        {isAuthenticated ? (
          <Stack.Screen
            name="Main"
            component={MainTabNavigator}
            options={{
              animationEnabled: false,
            }}
          />
        ) : (
          <Stack.Screen
            name="Login"
            component={LoginScreen}
            options={{
              animationEnabled: false,
            }}
          />
        )}
      </Stack.Navigator>
    </NavigationContainer>
  );
};

/**
 * Main App Component
 */
export default function App() {
  const [isAuthenticated, setIsAuthenticated] = React.useState(false);
  const [isLoading, setIsLoading] = React.useState(true);

  useEffect(() => {
    // Check authentication on app start
    const checkAuth = async () => {
      try {
        const token = await AsyncStorage.getItem('authToken');
        setIsAuthenticated(!!token);
      } catch (error) {
        console.error('Auth check failed:', error);
      } finally {
        setIsLoading(false);
      }
    };

    checkAuth();

    // Request push notification permissions
    requestUserPermission();
  }, []);

  /**
   * Request push notification permissions
   */
  const requestUserPermission = async () => {
    try {
      const authStatus = await messaging().requestPermission();
      const enabled =
        authStatus === messaging.AuthorizationStatus.AUTHORIZED ||
        authStatus === messaging.AuthorizationStatus.PROVISIONAL;

      if (enabled) {
        console.log('Push notifications enabled');
        const token = await messaging().getToken();
        console.log('FCM Token:', token);
        // Save token to backend
      }
    } catch (error) {
      console.error('Push notification error:', error);
    }
  };

  if (isLoading) {
    return null; // Show splash screen
  }

  return (
    <Provider store={store}>
      <PersistGate loading={null} persistor={persistor}>
        <RootNavigator isAuthenticated={isAuthenticated} />
      </PersistGate>
    </Provider>
  );
}
