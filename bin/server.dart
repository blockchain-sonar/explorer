// Copyright (c) 2021, the Dart project authors. Please see the AUTHORS file
// for details. All rights reserved. Use of this source code is governed by a
// BSD-style license that can be found in the LICENSE file.

// ignore_for_file: prefer_expression_function_bodies

import 'dart:convert';
import 'dart:io';

import 'package:mustache_template/mustache.dart';
import 'package:shelf/shelf.dart';
import 'package:shelf/shelf_io.dart' as shelf_io;
import 'package:shelf_router/shelf_router.dart' as shelf_router;
import 'package:shelf_static/shelf_static.dart' as shelf_static;

Future<void> main() async {
  // If the "PORT" environment variable is set, listen to it. Otherwise, 8080.
  // https://cloud.google.com/run/docs/reference/container-contract#port
  final port = int.parse(Platform.environment['PORT'] ?? '8080');

  // See https://pub.dev/documentation/shelf/latest/shelf/Cascade-class.html
  final cascade = Cascade()
      // First, serve files from the 'public' directory
      .add(_staticHandler)
      // If a corresponding file is not found, send requests to a `Router`
      .add(_router);

  // See https://pub.dev/documentation/shelf/latest/shelf_io/serve.html
  final server = await shelf_io.serve(
    // See https://pub.dev/documentation/shelf/latest/shelf/logRequests.html
    logRequests()
        // See https://pub.dev/documentation/shelf/latest/shelf/MiddlewareExtensions/addHandler.html
        .addHandler(cascade.handler),
    InternetAddress.anyIPv4, // Allows external connections
    port,
  );

  print('Serving at http://${server.address.host}:${server.port}');

  // Used for tracking uptime of the demo server.
  _watch.start();
}

// Serve files from the file system.
final _staticHandler = shelf_static.createStaticHandler(
  '../frontend',
  defaultDocument: 'index.html',
);

// Router instance to handler requests.
final _router = shelf_router.Router()
  ..get('/search', _search)
  ..get('/address/<address>', _address)
  ..get('/transaction/<transaction>', _transaction)
  ..get('/error/<error>', _error)
  ..get(
    '/time',
    (request) => Response.ok(DateTime.now().toUtc().toIso8601String()),
  )
  ..get('/info.json', _infoHandler)
  ..get('/sum/<a|[0-9]+>/<b|[0-9]+>', _sumHandler);

Future<Response> _search(Request request) async {
  final asset = request.url.queryParameters["q"];
  if (asset == "0xF0245F6251Bef9447A08766b9DA2B07b28aD80B0") {
    // await Future.delayed(const Duration(seconds: 3));
    // return Response.movedPermanently("/address");
    return Response(308, headers: {"location": "/address/$asset"});
  } else if (asset ==
      "0x25eb25e730b5c0f805ec3695040b6c8a2e1ec68effc884c3ec5b7e6dd038d1a8") {
    return Response(308, headers: {"location": "/transaction/$asset"});
  } else {
    return Response(308, headers: {"location": "/error/$asset"});
  }
}

Future<Response> _address(Request request, String address) async {
  final String source = await File('../frontend/address-1.html').readAsString();

  var template = Template(source, name: 'address');

  var output = template.renderString({
    "address": address,
    "assets": [
      {
        "id": "BNB",
        "balance": [
          {
            "amount": 0.10038,
            "value": 5,
          }
        ],
        "blockchains": [
          {
            "blockchain": "Binance Smart Coin",
            "token": false,
            "balance": [
              {
                "amount": 0.00038,
                "value": 1,
              }
            ],
            "alternatives": [
              {
                "name": "com.bscscan",
                "favicon": "https://bscscan.com/images/favicon.ico",
                "link":
                    "https://bscscan.com/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
              {
                "name": "io.binance.mintscan",
                "favicon": "https://binance.mintscan.io/favicon.ico",
                "link":
                    "https://binance.mintscan.io/account/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
            ],
          },
          {
            "blockchain": "Ethereum",
            "token": true,
            "balance": [
              {
                "amount": 0.1,
                "value": 4,
              }
            ],
            "alternatives": [
              {
                "name": "io.etherscan",
                "favicon": "https://etherscan.io/images/favicon3.ico",
                "link":
                    "https://etherscan.io/token/0xB8c77482e45F1F44dE1745F52C74426C631bDD52?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
              {
                "name": "io.explorer.bitquery",
                "favicon":
                    "https://bitquery.io/wp-content/uploads/2020/09/favicon.png",
                "link":
                    "https://explorer.bitquery.io/bsc/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
            ]
          }
        ],
        "name": "Binance Coin"
      },
      {
        "id": "BUSD-T",
        "balance": [
          {
            "amount": 0.219,
            "value": 2,
          }
        ],
        "blockchains": [
          {
            "blockchain": "Ethereum",
            "token": true,
            "balance": [
              {
                "amount": 0.219,
                "value": 2,
              }
            ],
            "alternatives": [
              {
                "name": "com.bscscan",
                "favicon": "https://bscscan.com/images/favicon.ico",
                "link":
                    "https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
              {
                "name": "io.explorer.bitquery",
                "favicon":
                    "https://bitquery.io/wp-content/uploads/2020/09/favicon.png",
                "link":
                    "https://explorer.bitquery.io/bsc/token/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
            ],
          }
        ],
        "name": "BUSD Token"
      },
      {
        "id": "ETH",
        "balance": [
          {
            "amount": 5.06587,
            "value": 15,
          }
        ],
        "blockchains": [
          {
            "blockchain": "Ethereum",
            "token": false,
            "balance": [
              {
                "amount": 4.06587,
                "value": 10,
              }
            ],
            "alternatives": [
              {
                "name": "io.etherscan",
                "favicon": "https://etherscan.io/images/favicon3.ico",
                "link":
                    "https://etherscan.io/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
              {
                "name": "io.ethplorer",
                "favicon": "https://ethplorer.io/icons-29d214c3/favicon.ico",
                "link":
                    "https://ethplorer.io/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
              {
                "name": "org.etherchain",
                "favicon": "https://beaconcha.in/favicon.ico",
                "link":
                    "https://etherchain.org/account/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
            ],
          },
          {
            "blockchain": "Binance Smart Coin",
            "token": true,
            "balance": [
              {
                "amount": 1.06587,
                "value": 5,
              }
            ],
            "alternatives": [
              {
                "name": "com.bscscan",
                "favicon": "https://bscscan.com/images/favicon.ico",
                "link":
                    "https://bscscan.com/token/0x2170ed0880ac9a755fd29b2688956bd959f933f8?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
            ]
          }
        ],
        "name": "Ether"
      },
      {
        "id": "MATIC",
        "balance": [
          {
            "amount": 56.124,
            "value": 25,
          }
        ],
        "blockchains": [
          {
            "blockchain": "Ethereum",
            "token": true,
            "balance": [
              {
                "amount": 50.124,
                "value": 15,
              }
            ],
            "alternatives": [
              {
                "name": "com.blockchain",
                "favicon":
                    "https://loutre.blockchair.io/assets/favicons/icon.svg",
                "link":
                    "https://blockchair.com/ethereum/erc-20/token/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
              {
                "name": "io.explorer.bitquery",
                "favicon":
                    "https://bitquery.io/wp-content/uploads/2020/09/favicon.png",
                "link":
                    "https://explorer.bitquery.io/matic/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
            ],
          },
          {
            "blockchain": "Polygon",
            "token": false,
            "balance": [
              {
                "amount": 6,
                "value": 10,
              }
            ],
            "alternatives": [
              {
                "name": "com.polygonscan",
                "favicon": "https://polygonscan.com/images/favicon.ico",
                "link":
                    "https://polygonscan.com/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
            ]
          }
        ],
        "name": "Polygon"
      },
      {
        "id": "USDT",
        "balance": [
          {
            "amount": 39,
            "value": 25,
          }
        ],
        "blockchains": [
          {
            "blockchain": "Ethereum",
            "token": true,
            "balance": [
              {
                "amount": 30,
                "value": 15,
              }
            ],
            "alternatives": [
              {
                "name": "io.etherscan",
                "favicon": "https://etherscan.io/images/favicon3.ico",
                "link":
                    "https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
              {
                "name": "io.ethplorer",
                "favicon": "https://ethplorer.io/icons-29d214c3/favicon.ico",
                "link":
                    "https://ethplorer.io/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
              {
                "name": "org.etherchain",
                "favicon": "https://beaconcha.in/favicon.ico",
                "link":
                    "https://etherchain.org/account/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
              },
            ],
          },
          {
            "blockchain": "Tron",
            "token": true,
            "balance": [
              {
                "amount": 9,
                "value": 10,
              }
            ],
            "alternatives": [
              {
                "name": "org.tronscan",
                "favicon": "https://tronscan.org/favicon.png?v=2",
                "link":
                    "https://tronscan.org/#/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e/"
              },
            ]
          }
        ],
        "name": "Tether"
      }
    ]
  });

  return Response.ok(output, headers: {"content-type": "text/html"});
}

Future<Response> _transaction(Request request, String transaction) async {
  final String source =
      await File('../frontend/transaction.html').readAsString();

  var template = Template(source, name: 'transaction');

  var output = template.renderString({
    "transaction": transaction,
    "explorers": [
      {
        "name": "io.etherscan",
        "favicon": "https://etherscan.io/images/favicon3.ico",
        "link":
            "https://etherscan.io/token/0xB8c77482e45F1F44dE1745F52C74426C631bDD52?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
      },
      {
        "name": "io.ethplorer",
        "favicon": "https://ethplorer.io/icons-29d214c3/favicon.ico",
        "link":
            "https://ethplorer.io/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
      },
    ]
  });

  return Response.ok(output, headers: {"content-type": "text/html"});
}

Future<Response> _error(Request request, String error) async {
  final String source = await File('../frontend/error.html').readAsString();

  var template = Template(source, name: 'error');

  var output = template.renderString({"error": error});

  return Response.ok(output, headers: {"content-type": "text/html"});
}

String _jsonEncode(Object? data) =>
    const JsonEncoder.withIndent(' ').convert(data);

const _jsonHeaders = {
  'content-type': 'application/json',
};

Response _sumHandler(Request request, String a, String b) {
  final aNum = int.parse(a);
  final bNum = int.parse(b);
  return Response.ok(
    _jsonEncode({'a': aNum, 'b': bNum, 'sum': aNum + bNum}),
    headers: {
      ..._jsonHeaders,
      'Cache-Control': 'public, max-age=604800, immutable',
    },
  );
}

final _watch = Stopwatch();

int _requestCount = 0;

final _dartVersion = () {
  final version = Platform.version;
  return version.substring(0, version.indexOf(' '));
}();

Response _infoHandler(Request request) => Response(
      200,
      headers: {
        ..._jsonHeaders,
        'Cache-Control': 'no-store',
      },
      body: _jsonEncode(
        {
          'Dart version': _dartVersion,
          'uptime': _watch.elapsed.toString(),
          'requestCount': ++_requestCount,
        },
      ),
    );
