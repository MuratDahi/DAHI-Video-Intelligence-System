import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class AnalysisCard extends StatelessWidget {
  final String title;
  final String value;
  final IconData icon;

  const AnalysisCard({
    super.key,
    required this.title,
    required this.value,
    required this.icon,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,

      padding: const EdgeInsets.all(22),

      decoration: BoxDecoration(
        color: const Color(0xff131E31),

        borderRadius: BorderRadius.circular(
          22,
        ),
      ),

      child: Column(
        crossAxisAlignment:
            CrossAxisAlignment.start,

        children: [

          //--------------------------------

          Row(
            children: [

              Icon(
                icon,
                color:
                    Colors.deepPurpleAccent,
                size: 28,
              ),

              const SizedBox(
                width: 12,
              ),

              Expanded(
                child: Text(
                  title,
                  style:
                      GoogleFonts.poppins(
                    color:
                        Colors.white,

                    fontWeight:
                        FontWeight.bold,

                    fontSize: 22,
                  ),
                ),
              ),
            ],
          ),

          //--------------------------------

          const SizedBox(
            height: 18,
          ),

          Text(
            value,

            style:
                GoogleFonts.poppins(
              color:
                  Colors.white70,

              fontSize: 17,

              height: 1.8,
            ),
          ),
        ],
      ),
    );
  }
}