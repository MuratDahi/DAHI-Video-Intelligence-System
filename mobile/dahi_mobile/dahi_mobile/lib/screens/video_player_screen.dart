import 'package:flutter/material.dart';
import 'package:video_player/video_player.dart';
import 'package:google_fonts/google_fonts.dart';
import '../widgets/analysis_card.dart';
import '../services/analysis_service.dart';

class VideoPlayerScreen extends StatefulWidget {
  final Map<String, dynamic> item;

  const VideoPlayerScreen({
    super.key,
    required this.item,
  });

  @override
  State<VideoPlayerScreen> createState() => _VideoPlayerScreenState();
}

class _VideoPlayerScreenState extends State<VideoPlayerScreen> {
  late VideoPlayerController controller;
  final AnalysisService analysisService = AnalysisService();
  Map<String, dynamic>? analysis;

  @override
  void initState() {
    super.initState();

    controller = VideoPlayerController.networkUrl(
      Uri.parse(
        "http://127.0.0.1:8000/videos/${widget.item["video_id"]}.mp4",
      ),
    )..initialize().then((_) {
        setState(() {});
        controller.play();
      });

    getAnalysis(
      widget.item["video_id"],
    );
  }

  Future<void> getAnalysis(String videoId) async {
    final result = await analysisService.getAnalysis(
      videoId,
    );

    print(
      result,
    );

    setState(() {
      analysis = result;
    });
  }

  @override
  void dispose() {
    controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xff08111F),
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        title: Text(
          widget.item["title"],
        ),
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              //----------------------------------
              // VIDEO
              //----------------------------------
              controller.value.isInitialized
                  ? ClipRRect(
                      borderRadius: BorderRadius.circular(30),
                      child: AspectRatio(
                        aspectRatio: controller.value.aspectRatio,
                        child: VideoPlayer(controller),
                      ),
                    )
                  : const Center(
                      child: CircularProgressIndicator(
                        color: Colors.white,
                      ),
                    ),

              const SizedBox(height: 25),
              const SizedBox(height: 10),

              Text(
                "DAHI",
                style: GoogleFonts.poppins(
                  color: Colors.white,
                  fontSize: 34,
                  fontWeight: FontWeight.bold,
                ),
              ),

              const SizedBox(height: 10),

              Text(
                "DAHI Video Analysis Report",
                style: GoogleFonts.poppins(
                  color: Colors.white70,
                  fontSize: 18,
                ),
              ),

              const SizedBox(height: 25),
              const SizedBox(height: 10),

              //----------------------------------
              // SÜRE
              //----------------------------------
              _infoCard(
                Icons.schedule,
                "Süre",
                "${widget.item["duration"]} saniye",
              ),

              const SizedBox(height: 15),

              //----------------------------------
              // VIDEO TITLE
              //----------------------------------
              _infoCard(
                Icons.video_collection,
                "Video Title",
                widget.item["title"],
              ),

              const SizedBox(height: 15),

              //----------------------------------
              // SIMILARITY SCORE
              //----------------------------------
              _infoCard(
                Icons.auto_awesome,
                "Similarity Score",
                "${(widget.item["score"] * 100).toStringAsFixed(1)} %",
              ),

              const SizedBox(height: 30),

              //----------------------------------
              // ANALYSIS
              //----------------------------------
              if (analysis == null)
                const Center(
                  child: CircularProgressIndicator(
                        color: Colors.white,
                  ),
                )
              else ...[
                //----------------------------------
                // OCR REPORT
                //----------------------------------
                AnalysisCard(
                  title: "OCR REPORT",
                  value: analysis?["ocr_report"] ?? "OCR raporu hazırlanamadı.",
                  icon: Icons.document_scanner,
                ),

                const SizedBox(height: 25),
                const SizedBox(height: 10),

                //----------------------------------
                // SPEECH REPORT
                //----------------------------------
                AnalysisCard(
                  title: "SPEECH REPORT",
                  value: analysis?["speech_report"] ?? "Konuşma raporu hazırlanamadı.",
                  icon: Icons.mic,
                ),

                const SizedBox(height: 25),
                const SizedBox(height: 10),

                //----------------------------------
                // OBJECT REPORT
                //----------------------------------
                AnalysisCard(
                  title: "OBJECT REPORT",
                  value: analysis?["object_report"] ?? "Nesne raporu hazırlanamadı.",
                  icon: Icons.visibility,
                ),

                const SizedBox(height: 25),
                const SizedBox(height: 10),

                //----------------------------------
                // VIDEO INFORMATION
                //----------------------------------
                AnalysisCard(
                  title: "VIDEO INFORMATION",
                  value: analysis?["video_report"] ?? "Video bilgileri hazırlanamadı.",
                  icon: Icons.analytics,
                ),

                const SizedBox(height: 25),
                const SizedBox(height: 10),

                //----------------------------------
                // SCENE REPORT
                //----------------------------------
                AnalysisCard(
                  title: "SCENE REPORT",
                  value: analysis?["scene_report"] ?? "Sahne raporu hazırlanamadı.",
                  icon: Icons.movie,
                ),

                const SizedBox(height: 25),
                const SizedBox(height: 10),

                //----------------------------------
                // VIDEO CATEGORY
                //----------------------------------
                AnalysisCard(
                  title: "VIDEO CATEGORY",
                  value: analysis?["video_category"] ?? "Kategori bulunamadı.",
                  icon: Icons.category,
                ),

                const SizedBox(height: 25),
                const SizedBox(height: 10),

                //----------------------------------
                // DAHI ANALYSIS REPORT
                //----------------------------------
                AnalysisCard(
                  title: "DAHI ANALYSIS REPORT",
                  value: analysis?["insight"] ?? "DAHI raporu hazırlanamadı.",
                  icon: Icons.psychology,
                ),
              ]
            ],
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          setState(() {
            controller.value.isPlaying
                ? controller.pause()
                : controller.play();
          });
        },
        child: Icon(
          controller.value.isPlaying ? Icons.pause : Icons.play_arrow,
        ),
      ),
    );
  }

  Widget _infoCard(
    IconData icon,
    String title,
    String value,
  ) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: const Color(0xff111827),
        borderRadius: BorderRadius.circular(30),
      ),
      child: Row(
        children: [
          Icon(
            icon,
            color: Colors.blueAccent,
          ),
          const SizedBox(width: 15),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  title,
                  style: GoogleFonts.poppins(
                    color: Colors.white60,
                  ),
                ),
                Text(
                  value,
                  style: GoogleFonts.poppins(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                    fontSize: 20,
                  ),
                ),
              ],
            ),
          )
        ],
      ),
    );
  }

  Widget _section(
    String title,
    String text,
  ) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: const Color(0xff111827),
        borderRadius: BorderRadius.circular(30),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            title,
            style: GoogleFonts.poppins(
              color: Colors.white,
              fontWeight: FontWeight.bold,
              fontSize: 20,
            ),
          ),
          const SizedBox(height: 10),
          Text(
            text,
            style: GoogleFonts.poppins(
              color: Colors.white70,
              height: 1.5,
            ),
          )
        ],
      ),
    );
  }
}