import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class VideoCard extends StatelessWidget {
  final Map<String, dynamic> item;
  final VoidCallback onPressed;

  const VideoCard({
    super.key,
    required this.item,
    required this.onPressed,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 20),
      decoration: BoxDecoration(
        color: const Color(0xff131E31),
        borderRadius: BorderRadius.circular(22),
        border: Border.all(
          color: Colors.white10,
        ),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [

          //-------------------------------
          // Thumbnail
          //-------------------------------

          ClipRRect(
            borderRadius: const BorderRadius.only(
              topLeft: Radius.circular(22),
              topRight: Radius.circular(22),
            ),
            child: Image.network(

              "http://127.0.0.1:8000/images/${item["video_id"]}/scene_001.jpg",

              height: 220,

              width: double.infinity,

              fit: BoxFit.cover,

              errorBuilder: (_, __, ___) {

                return Container(

                  height: 220,

                  color: const Color(0xff232F45),

                  child: const Center(

                    child: Icon(

                      Icons.broken_image,

                      color: Colors.white,

                      size: 60,

                    ),

                  ),

                );

              },

            ),
          ),

          Padding(
            padding: const EdgeInsets.all(18),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [

                Text(
                  item["title"],
                  style: GoogleFonts.poppins(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                    fontSize: 22,
                  ),
                ),

                const SizedBox(height: 10),

                LinearProgressIndicator(
                  value: item["score"],
                  minHeight: 8,
                  borderRadius: BorderRadius.circular(20),
                  backgroundColor: Colors.white12,
                  valueColor: const AlwaysStoppedAnimation(
                    Color(0xff6D5DF6),
                  ),
                ),

                const SizedBox(height: 12),

                    Row(
                      children: [

                        const Icon(
                          Icons.schedule,
                          color: Colors.white54,
                          size: 18,
                        ),

                        const SizedBox(width: 6),

                        Text(
                          "${item["duration"]} saniye",
                          style: GoogleFonts.poppins(
                            color: Colors.white70,
                          ),
                        ),

                      ],
                    ),

const SizedBox(height: 8),

Text(
  "Benzerlik ${(item["score"] * 100).toStringAsFixed(1)}%",
  style: GoogleFonts.poppins(
    color: Colors.white70,
    fontWeight: FontWeight.w600,
  ),
),

                const SizedBox(height: 18),

                SizedBox(
                  width: double.infinity,
                  height: 52,
                  child: ElevatedButton.icon(
                    onPressed: onPressed,
                    icon: const Icon(Icons.play_arrow),
                    label: const Text("Videoyu Aç"),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}