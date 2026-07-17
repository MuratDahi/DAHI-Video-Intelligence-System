import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

import 'screens/home_screen.dart';

void main() {
  runApp(const DahiApp());
}

class DahiApp extends StatelessWidget {
  const DahiApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: "DAHI",
      theme: ThemeData(
        brightness: Brightness.dark,
        scaffoldBackgroundColor: const Color(0xff0F172A),

        textTheme: GoogleFonts.poppinsTextTheme(
          ThemeData.dark().textTheme,
        ),

        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xff6366F1),
          brightness: Brightness.dark,
        ),

        useMaterial3: true,
      ),
      home: const HomeScreen(),
    );
  }
}