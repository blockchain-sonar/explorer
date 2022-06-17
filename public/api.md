# Blockchain Sonar's Explorer API

## Basics

* Data is returned in ascending order. Oldest first, newest last.
* All time and timestamp related fields are in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601).
* For GET endpoints, parameters must be sent as a [query string](https://en.wikipedia.org/wiki/Query_string).
* For POST, PUT, and DELETE endpoints, the parameters are sent in the request body with content type `application/json`.
* Success request codes: 2XX
* Client's mistakes: 4XX
* Server's errors: 5XX

!!! warning
	Almost POST requests are idempotent. Any duplicate request will be completed with response 
	of the first request within 24 hours from the first request. This behaviour in conclusion
	with client identifier avoids potential duplicates.


### Responses
Our API uses [HTTP status codes](http://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) to indicate the status of your requests. This includes successful and unsuccessful responses.

* 2xx (Successful): The request was successfully received, understood, and accepted
* 4xx (Client Error): The request contains bad syntax or cannot be fulfilled
* 5xx (Server Error): The server failed to fulfill an apparently valid request

!!! note "5xx"
	It is important to NOT treat this as a failure operation. The execution status is UNKNOWN and could have been a success.

!!! note "Error Reason Phrase"
	An unsuccessful response DOES NOT HAVE body. Error message passed via [Reason Phrase](https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html) along with Status Code and **REASON-PHRASE** header

| **Status Code**            | **Meaning**                                                                              |
|----------------------------|------------------------------------------------------------------------------------------|
| 200 OK                     | Standard response for successful HTTP requests                                           |
| 201 Created                | The request has been fulfilled, resulting in the creation of a new resource              |
| 202 Accepted               | The request has been accepted for processing, but the processing has not been completed  |
| 400 Bad Request            | The server cannot or will not process the request due to an apparent client error (e.g., malformed request syntax, size too large, invalid request message framing, or deceptive request routing)   |
| 401 {{Reason Phrase}}      | Most likely you wasn't able to construct and sign your API request correctly using HMAC  |
| 403 Forbidden              | You don't have required permissions to perform requested action on the resource          |
| 404 Not Found              | We don't have the resource you've requested                                              |
| 409 {{Reason Phrase}}      | Most likely the client's identifier value you're trying to use had been used before      |
| 422 {{Reason Phrase}}      | The request was well-formed but was unable to be followed due to semantic errors         |
| 500 {{Reason Phrase}}      | We have a problem with our server                                                        |
| 503 Service Unavailable    | We're temporarily offline for maintenance                                                |

### Pagination

TBD

### Types

#### Dates

All timestamps from API are returned in [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601) with milliseconds. Make sure you can parse the following ISO 8601 format. Most modern languages and libraries will handle this without issues.

```JSON
{
	"date": "2020-01-16T07:35:32.129Z"
}
```

#### Decimal (Financial)
All numbers that represent financial values are returned as strings to preserve full precision across platforms. When making a request, you must convert your numbers to strings to avoid truncation and precision errors.

```JSON
{
	"amount": "12345678.12345678"
}
```

#### Integer
Integer numbers (like counter) are unquoted.

```JSON
{
	"confirmations": 5
}
```

### Rate Limit
When a rate limit is exceeded, a status of **429 Too Many Requests** will be returned.

TBD: what is limit?


## Authentication

TBD

## /v1/address

### Fetch address information

Retrieve an information about `blockchain address`.

```
GET /v1/address/{blockchain_address}
```

**URL Parameters:**

| **Name**                | **Description**                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| **blockchain_address**  | Blockchain address like `0x2b6828f4f227953fb36f42bda830b457afdc1c5e`, `3GfSyzYpHzQKn8Ey3GVxFZrpTV93KUC1HE` etc.  |

**Query Parameters:**

| **Name**         | **Type**   | **Mandatory**  | **Description**                           |
|------------------|------------|----------------|-------------------------------------------|
| **asset**        | STRING     | NO             | Asset identifier like `ETH`, `USDT` etc.  |

```
--->
GET /explorer/v1/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e HTTP/1.0
Host: api.blockchain-sonar-test.com
Accept: application/json


<--
HTTP/1.1 200 OK
Content-Type: application/json

{
	"address": "0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
	"assets": {
		"ETH": {
			"balance": "0.001892326486858519",
			"alternatives": {
				"com.blockchair": "https://blockchair.com/ethereum/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
				"com.blockcypher": "https://live.blockcypher.com/eth/address/2b6828f4f227953fb36f42bda830b457afdc1c5e/",
				"io.etherscan": "https://etherscan.io/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
				"io.ethplorer": "https://ethplorer.io/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e",
				"org.etherchain": "https://etherchain.org/account/2b6828f4f227953fb36f42bda830b457afdc1c5e"
			}
		},
		"USDT": {
			"balance": "454.241859",
			"alternatives": {
				"io.etherscan": "https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
			}
		},
		"BNB": {
			"balance": "0",
			"alternatives": {
				"com.bscscan": "https://bscscan.com/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
			}
		},
		"BUSD-T": {
			"balance": "0",
			"alternatives": {
				"com.bscscan": "https://bscscan.com/token/0x55d398326f99059ff775485246999027b3197955?a=0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
			}
		},
		,
		"MATIC": {
			"balance": "0",
			"alternatives": {
				"com.polygonscan": "https://polygonscan.com/address/0x2b6828f4f227953fb36f42bda830b457afdc1c5e"
			}
		},
		
	}
}
```

## /v1/asset

### List assets

```
--->
GET /explorer/v1/asset HTTP/1.0
Host: api.blockchain-sonar-test.com
Accept: application/json


<--
HTTP/1.1 200 OK
Content-Type: application/json

{
	"ETH": {
		"name": "Ether"
	},
	"USDT": {
		"name": "Tether USD"
	},
	"BNB": {
		"name": "Binance Coin"
	},
	"BUSD-T": {
		"name": "BUSD-T Stablecoin"
	},
	"MATIC": {
		"name": "MATIC"
	}
}
```

### Fetch asset

```
GET /v1/asset/{asset_identifier}
```

**URL Parameters:**

| **Name**                | **Description**                                   |
|-------------------------|---------------------------------------------------|
| **asset_identifier**    | Blockchain address like `ETH`, `USDT` etc.        |

```
--->
GET /explorer/v1/asset/USDT HTTP/1.0
Host: api.blockchain-sonar-test.com
Accept: application/json


<--
HTTP/1.1 200 OK
Content-Type: application/json

{
	"name": "Tether USD"
}
```

