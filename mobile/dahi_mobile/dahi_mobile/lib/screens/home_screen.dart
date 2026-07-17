import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../services/api_service.dart';
import 'video_player_screen.dart';
import '../widgets/video_card.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final TextEditingController searchController = TextEditingController();
  final api = ApiService();
  List<dynamic> searchResults = [];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xff08111F),
      body: Stack(
        children: [
          //--------------------------------
          // PURPLE GLOW TOP RIGHT
          //--------------------------------
          Positioned(
            top: -160,
            right: -120,
            child: ImageFiltered(
              imageFilter: ImageFilter.blur(
                sigmaX: 120,
                sigmaY: 120,
              ),
              child: Container(
                width: 280,
                height: 280,
                decoration: const BoxDecoration(
                  color: Color(0xff7C3AED),
                  shape: BoxShape.circle,
                ),
              ),
            ),
          ),

          //--------------------------------
          // BLUE GLOW TOP LEFT
          //--------------------------------
          Positioned(
            top: -110,
            left: -130,
            child: ImageFiltered(
              imageFilter: ImageFilter.blur(
                sigmaX: 100,
                sigmaY: 100,
              ),
              child: Container(
                width: 220,
                height: 220,
                decoration: const BoxDecoration(
                  color: Color(0xff2563EB),
                  shape: BoxShape.circle,
                ),
              ),
            ),
          ),

          //--------------------------------
          // CONTENT
          //--------------------------------
          SafeArea(
            child: SingleChildScrollView(
              child: Padding(
                padding: const EdgeInsets.symmetric(
                  horizontal: 24,
                  vertical: 20,
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const SizedBox(height: 15),

                    //--------------------------------
                    // HEADER
                    //--------------------------------
                    Row(
                      children: [
                        Container(
                          width: 60,
                          height: 60,
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(20),
                            gradient: const LinearGradient(
                              colors: [
                                Color(0xff8B5CF6),
                                Color(0xff6366F1),
                              ],
                            ),
                            boxShadow: [
                              BoxShadow(
                                color: const Color(0xff6366F1).withOpacity(.45),
                                blurRadius: 35,
                              )
                            ],
                          ),
                          child: const Icon(
                            Icons.auto_awesome,
                            color: Colors.white,
                            size: 30,
                          ),
                        ),
                        const SizedBox(width: 18),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                "Merhaba Murat 👋",
                                style: GoogleFonts.poppins(
                                  color: Colors.white70,
                                  fontSize: 15,
                                ),
                              ),
                              const SizedBox(height: 4),
                              Text(
                                "DAHI AI Search",
                                style: GoogleFonts.poppins(
                                  color: Colors.white,
                                  fontWeight: FontWeight.bold,
                                  fontSize: 28,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),

                    const SizedBox(height: 40),

                    //--------------------------------
                    // TITLE
                    //--------------------------------
                    Text(
                      "Video,\nKonuşma ve OCR\nile Akıllı Arama",
                      style: GoogleFonts.poppins(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        height: 1.15,
                        fontSize: 36,
                      ),
                    ),
                    const SizedBox(height: 15),
                    Text(
                      "Yapay zekâ destekli multimodal video arama sistemi.",
                      style: GoogleFonts.poppins(
                        color: Colors.white60,
                        fontSize: 16,
                        height: 1.6,
                      ),
                    ),

                    const SizedBox(height: 35),

                    //--------------------------------
                    // SEARCH BOX
                    //--------------------------------
                    Container(
                      height: 62,
                      decoration: BoxDecoration(
                        color: const Color(0xff131E31),
                        borderRadius: BorderRadius.circular(18),
                        border: Border.all(
                          color: Colors.white10,
                        ),
                      ),
                      child: TextField(
                        controller: searchController,
                        style: GoogleFonts.poppins(
                          color: Colors.white,
                        ),
                        decoration: InputDecoration(
                          border: InputBorder.none,
                          hintText: "Video ara...",
                          hintStyle: GoogleFonts.poppins(
                            color: Colors.white54,
                          ),
                          prefixIcon: const Icon(
                            Icons.search,
                            color: Colors.white70,
                          ),
                          suffixIcon: const Icon(
                            Icons.mic_none,
                            color: Colors.white70,
                          ),
                        ),
                      ),
                    ),

                    const SizedBox(height: 22),

                    //--------------------------------
                    // BUTTON
                    //--------------------------------
                    SizedBox(
                      width: double.infinity,
                      height: 58,
                      child: ElevatedButton(
                       onPressed: () async {

                        print("BUTONA BASILDI");

                        try {

                          final results = await api.search(
                            searchController.text,
                            5,
                          );

                          print(results);

                          setState(() {
                            searchResults = results;
                          });

                        } catch (e) {

                          print("HOME SCREEN HATASI");
                          print(e);

                        }

                      },
                        style: ElevatedButton.styleFrom(
                          elevation: 0,
                          backgroundColor: const Color(0xff6D5DF6),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(18),
                          ),
                        ),
                        child: Text(
                          "ARA",
                          style: GoogleFonts.poppins(
                            color: Colors.white,
                            fontSize: 18,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    ),

                    const SizedBox(height: 35),

                    //--------------------------------
                    // QUICK STATS
                    //--------------------------------
                    Row(
                      children: [
                        Expanded(
                          child: _statCard(
                            "12K+",
                            "Video",
                            Icons.video_collection_rounded,
                          ),
                        ),
                        const SizedBox(width: 15),
                        Expanded(
                          child: _statCard(
                            "98%",
                            "Doğruluk",
                            Icons.auto_graph,
                          ),
                        ),
                      ],
                    ),

                    const SizedBox(height: 35),

                    //--------------------------------
                    // TREND SEARCHES
                    //--------------------------------
                    Text(
                      "🔥 Trend Aramalar",
                      style: GoogleFonts.poppins(
                        color: Colors.white,
                        fontSize: 20,
                        fontWeight: FontWeight.w700,
                      ),
                    ),
                    const SizedBox(height: 18),
                    SizedBox(
                      height: 44,
                      child: ListView(
                        scrollDirection: Axis.horizontal,
                        children: [
                          _trendChip("Fitness"),
                          _trendChip("Yapay Zeka"),
                          _trendChip("Yazılım"),
                          _trendChip("Komedi"),
                          _trendChip("Futbol"),
                        ],
                      ),
                    ),

                    const SizedBox(height: 35),

                    //--------------------------------
                    // RECENT SEARCHES
                    //--------------------------------
                    Text(
                      "📌 Son Aramalar",
                      style: GoogleFonts.poppins(
                        color: Colors.white,
                        fontSize: 20,
                        fontWeight: FontWeight.w700,
                      ),
                    ),
                    const SizedBox(height: 18),
                    _recentSearchCard(
                      title: "Fitness Motivation",
                      subtitle: "2 dakika önce",
                      icon: Icons.fitness_center,
                    ),
                    _recentSearchCard(
                      title: "Python Tutorial",
                      subtitle: "Bugün",
                      icon: Icons.code,
                    ),
                    _recentSearchCard(
                      title: "Komik Videolar",
                      subtitle: "Dün",
                      icon: Icons.emoji_emotions,
                    ),
                    const SizedBox(height: 30),

                    //--------------------------------
                    // AI RECOMMENDATIONS
                    //--------------------------------
                    Text(
                      "🤖 AI Önerileri",
                      style: GoogleFonts.poppins(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        fontSize: 22,
                      ),
                    ),
                    const SizedBox(height: 18),
                    SizedBox(
                      height: 220,
                      child: ListView(
                        scrollDirection: Axis.horizontal,
                        children: [
                          _aiCard(
                            title: "Fitness Motivation",
                            subtitle: "0.98 Match",
                            color: const Color(0xff6D5DF6),
                          ),
                          _aiCard(
                            title: "Python Tutorial",
                            subtitle: "0.95 Match",
                            color: const Color(0xff2563EB),
                          ),
                          _aiCard(
                            title: "Football Skills",
                            subtitle: "0.93 Match",
                            color: const Color(0xffEC4899),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 40),

                    //--------------------------------
                    // SEARCH RESULTS
                    //--------------------------------
                    if (searchResults.isNotEmpty) ...[
                      const SizedBox(height: 25),
                      Text(
                        "Arama Sonuçları",
                        style: GoogleFonts.poppins(
                          color: Colors.white,
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(height: 20),
                      ...searchResults.map((item) {

                      return VideoCard(

                        item: item,

                        onPressed: () {

                          Navigator.push(

                            context,

                            MaterialPageRoute(

                              builder: (_) => VideoPlayerScreen(

                                item : item,

                              ),

                            ),

                          );

                        },

                      );

                    }), 
                    ],
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  //--------------------------------
  // WIDGET HELPER METHODS
  //--------------------------------

  Widget _statCard(String value, String title, IconData icon) {
    return Container(
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: const Color(0xff131E31),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(
          color: Colors.white10,
        ),
      ),
      child: Column(
        children: [
          Icon(
            icon,
            color: const Color(0xff8B5CF6),
            size: 30,
          ),
          const SizedBox(height: 15),
          Text(
            value,
            style: GoogleFonts.poppins(
              color: Colors.white,
              fontSize: 26,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            title,
            style: GoogleFonts.poppins(
              color: Colors.white60,
            ),
          )
        ],
      ),
    );
  }

  Widget _trendChip(String title) {
    return Container(
      margin: const EdgeInsets.only(right: 12),
      padding: const EdgeInsets.symmetric(
        horizontal: 18,
        vertical: 10,
      ),
      decoration: BoxDecoration(
        color: const Color(0xff151F32),
        borderRadius: BorderRadius.circular(30),
      ),
      child: Center(
        child: Text(
          title,
          style: GoogleFonts.poppins(
            color: Colors.white,
            fontWeight: FontWeight.w500,
          ),
        ),
      ),
    );
  }

  Widget _recentSearchCard({
    required String title,
    required String subtitle,
    required IconData icon,
  }) {
    return Container(
      margin: const EdgeInsets.only(bottom: 15),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: const Color(0xff131E31),
        borderRadius: BorderRadius.circular(18),
        border: Border.all(
          color: Colors.white10,
        ),
      ),
      child: Row(
        children: [
          Container(
            width: 52,
            height: 52,
            decoration: BoxDecoration(
              color: const Color(0xff6D5DF6),
              borderRadius: BorderRadius.circular(14),
            ),
            child: Icon(
              icon,
              color: Colors.white,
            ),
          ),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: GoogleFonts.poppins(
                    color: Colors.white,
                    fontWeight: FontWeight.w600,
                    fontSize: 16,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  subtitle,
                  style: GoogleFonts.poppins(
                    color: Colors.white54,
                    fontSize: 13,
                  ),
                ),
              ],
            ),
          ),
          const Icon(
            Icons.arrow_forward_ios_rounded,
            color: Colors.white38,
            size: 18,
          ),
        ],
      ),
    );
  }

  Widget _aiCard({
    required String title,
    required String subtitle,
    required Color color,
  }) {
    return Container(
      width: 220,
      margin: const EdgeInsets.only(right: 18),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(24),
        gradient: LinearGradient(
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
          colors: [
            color,
            color.withOpacity(.55),
          ],
        ),
        boxShadow: [
          BoxShadow(
            color: color.withOpacity(.35),
            blurRadius: 25,
            offset: const Offset(0, 10),
          )
        ],
      ),
      child: Padding(
        padding: const EdgeInsets.all(22),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Spacer(),
            Container(
              width: 55,
              height: 55,
              decoration: BoxDecoration(
                color: Colors.white24,
                borderRadius: BorderRadius.circular(16),
              ),
              child: const Icon(
                Icons.smart_toy,
                color: Colors.white,
              ),
            ),
            const SizedBox(height: 20),
            Text(
              title,
              style: GoogleFonts.poppins(
                color: Colors.white,
                fontSize: 21,
                fontWeight: FontWeight.bold,
              ),
            ),
            const SizedBox(height: 8),
            Text(
              subtitle,
              style: GoogleFonts.poppins(
                color: Colors.white70,
                fontSize: 15,
              ),
            ),
          ],
        ),
      ),
    );
  }
}