 import 'package:dio/dio.dart';

class ApiService {
  final Dio dio = Dio(
    BaseOptions(
      baseUrl: "http://127.0.0.1:8000",
    ),
  );

  Future<List<dynamic>> search(
    String query,
    int topK,
  ) async {

    print("API ISTEK GONDERILIYOR");

    try {

      final response = await dio.post(
        "/search",
        data: {
          "query": query,
          "top_k": topK,
        },
      );

      print("API CEVABI:");
      print(response.data);

      return response.data;

    } catch (e) {

      print("HATA OLUSTU");
      print(e);

      rethrow;

    }

  }
}