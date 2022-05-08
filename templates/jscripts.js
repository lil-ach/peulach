// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCXBR_0_UQhRsq9_Z75rKY9Z8gO7f-FYh0",
  authDomain: "test-fcfc1.firebaseapp.com",
  projectId: "test-fcfc1",
  storageBucket: "test-fcfc1.appspot.com",
  messagingSenderId: "475633284013",
  appId: "1:475633284013:web:412f26593b6b38ceffe724"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
document.write("initializeApp succeeded")