import 'package:dio/dio.dart';

class AnalysisService {
  final Dio dio = Dio(
    BaseOptions(
      baseUrl: "http://127.0.0.1:8000",
    ),
  );

  Future<dynamic> getAnalysis(
    String videoId,
  ) async {
    final response = await dio.get(
      "/analysis/$videoId",
    );

    return response.data;
  }
}