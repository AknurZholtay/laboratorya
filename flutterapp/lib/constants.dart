import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Constants {
  static const String baseUrl = 'http://127.0.0.1:8000/';
}

class SomeWidget extends StatelessWidget {
  const SomeWidget({super.key});
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      onPressed: () async {
        // ignore: unused_local_variable
        final response =
            await http.get(Uri.parse('${Constants.baseUrl}/login'));
      },
      child: const Text('Make Request'),
    );
  }
}
