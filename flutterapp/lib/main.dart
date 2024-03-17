import 'package:flutter/material.dart';
import 'package:flutterapp/login_screen.dart'; // Import your LoginScreen widget

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter App',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home:
          const LoginScreen(), // Set the home property to your LoginScreen widget
    );
  }
}
