

from app.application import lambda_handler

#record = {'Records': [{'messageId': 'bbc1b650-e8f2-4710-8ea5-244d2e824bfa', 'receiptHandle': 'AQEBVB74n/omna5EeIYexPI5FzYAg1Yh+Gzj5SgNE+cBoarPxnVQpKeHgSSko4zB43wxrm6sJP+0cOgTMkeJWUDtl3wshyt9sZjn9nnk1hWyY4ry78cAgUPXUylFFhaqWn4mUiKtNEARR/HxtU84PHw6xiMl+l0YuhkofoRaylWCdLtEpx19ZFfDuwyID/FjnJ2qIaY7QMC3KRQQ7AfOEsE7p84Uc9WJoRs852q/+yJPI/Jw9jVz2BjqGpI0eF0DZZVvTv3AV3R5cSF9H7cMQdpPmBK00OYQ0VPNUCedio+9RR77myoivIEZz1bLuVE08Dwai1k9OdGqdETOFrLLq9iFIQzwOYtm0DxmDV/3dCeNSL6U7AwAA+EJ9mVTBat52pyh', 'body': '{\n  "id": 10,\n  "name": "name1"\n}', 'attributes': {'ApproximateReceiveCount': '1', 'SentTimestamp': '1677294576861', 'SenderId': '669676830092', 'ApproximateFirstReceiveTimestamp': '1677294576871'}, 'messageAttributes': {}, 'md5OfBody': '2b4a6f8d24c37bacdfab7f2edb7180d5', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws:sqs:us-east-1:669676830092:sqsQueue', 'awsRegion': 'us-east-1'}]}
#record = {'Records': [{'messageId': 'bfa994de-9f43-4f69-947a-af13d991dae5', 'receiptHandle': 'AQEB1dCZJXILOmalC+1UKQSeom3past9zJikoU6SdlATS4iHWNwHEQxLSKqd4mXSRcN/tpAsjqnC6BToIBge1HQmkK6jFsr1pHkzLyWSxdIWTdL/y/f2B2Xfc/uM0YBVVF7oOwIfJPyJkQ+2zpsyuLNOM334NZhUNeAEXnM81Sxwq4Lya2+Y8AvdQc80rSV00h7JZbvjcT60n4X6VXlSUERtDlMkwBcS8LvvJJqEG0Eul6eEgiyeP4j2YBQ3Dv84qK4V+VSGVRO6uAd3yQSivJl2OrnVTMPhAZypdIHv5ur8OyYnstC4monOBuj5878S6i5N68J/rGpTb0wLS8IWq5HLQK+8kEbrJZy+V7HQuqWIkqccdUb9X4AerPjM3opWj+v4', 'body': '{\n    "contrato": {\n        "NumContrato": "1221112232",\n        "Serie": 22,\n        "id": "1223",\n        "dataContratacao": "10-10-2022"\n    }\n}', 'attributes': {'ApproximateReceiveCount': '1', 'SentTimestamp': '1677299769082', 'SenderId': '669676830092', 'ApproximateFirstReceiveTimestamp': '1677299769096'}, 'messageAttributes': {}, 'md5OfBody': 'e1f37ece13606e86ec845f30097068af', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws:sqs:us-east-1:669676830092:sqsQueue', 'awsRegion': 'us-east-1'}]}
#record = {'Records': [{'messageId': '58b4580d-1fa2-4249-99bd-cc2b9e5d6f28', 'receiptHandle': 'AQEBtQJ13W80r3WJGpdcMOs/B2G/E117lk9OnJj2lU+/Pw62xiyNmfFCUCfWhmWyb7YJaRj2XZ3dL1C4GoBC89MM/rQ5JeovrKEYJeWIImRTe3sX3Usvdl+IEti684cgwbsEIBMQpNRwv43/0bG8zP4CTzsABmohgAdvKQUjdDcTqaBCKXcShZa5i6dAZx8sk2Szd7DLbbyrq8ukuyOCSJGTMCRA6myHArtRtqvGVqgcQTFLWXJ7maU706cQxus8m3bCVtZo8ErWJx8e1ZvgRFhideclsUQKmunOsyIvoTucX1Iw1qtau6YOq5i2Rp91PEC1PJX22uaVn14aj2IAo3vr3eRbS1pnircfSoZ59KmJkycPaCCt/FvMvmasnhqXfe7z', 'body': '{\n    "contrato": [\n        {\n            "NumContrato": "1221112232",\n            "Serie": 22,\n            "id": "1223",\n            "dataContratacao": "10-10-2022"\n        },\n        {\n            "NumContrato": "22222222",\n            "Serie": 33,\n            "id": "2312",\n            "dataContratacao": "15-01-2022"\n        }\n    ]\n}', 'attributes': {'ApproximateReceiveCount': '1', 'SentTimestamp': '1677304430960', 'SenderId': '669676830092', 'ApproximateFirstReceiveTimestamp': '1677304430970'}, 'messageAttributes': {}, 'md5OfBody': '67dde2c25e5498d73988e1ade245daea', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws:sqs:us-east-1:669676830092:sqsQueue', 'awsRegion': 'us-east-1'}]}
record = {'Records': [{'messageId': '6ce49fd0-c169-44e7-909f-3b0ad35b9252', 'receiptHandle': 'AQEBNWki4Z9tjOXHxZUUyamDphWYaMlZNRN22ta826nyTOGa7OpODvf6F9xFfJOnIqB1x5bf22KrdE5OPsEcZwcimDlKzNr0DLndxA+858vGliDhvNGG+wbmRfZ75uqfjXkmQ/bW4JuJuBsB/ajsviI2fZJPA+ZMMYFLxaso8MLRz5GSF9Zf/vjp371sm/1bzZPS3Qfp1M193KWaEDxuGmW8JYKVRP5h39JyH6VwZNdI1Gc5BObMYqWud94kvezv5C5hrx7JHw5h9hfxu2JzFEOQCUzOdL7tDBCiKFOKyPxiMbbxuVJ3DzUxIJYsPe7uZ0fop2C59d8TYli5/07Ez4zaCVQLJwt/yiPaNN59NDKQBMpHtF9lk8VpqZiUPJaXLjjw', 'body': '{\n    "contrato": [\n        {\n            "NumContrato": "1221112232",\n            "Serie": 22,\n            "id": "1223",\n            "dataContratacao": "10-10-2022"\n        },\n        {\n            "NumContrato": "22222222",\n            "Serie": 33,\n            "id": "2312",\n            "dataContratacao": "15-01-2022"\n        }\n    ],\n    "parcela": [\n        {\n            "NumContrato": "1221112232",\n            "Parcela": 22,\n            "qtdParcela": "320"\n        },\n        {\n            "NumContrato": "22222222",\n            "Parcela": 23,\n            "qtdParcela": "320"\n        }\n    ]\n}', 'attributes': {'ApproximateReceiveCount': '1', 'SentTimestamp': '1677463697045', 'SenderId': '669676830092', 'ApproximateFirstReceiveTimestamp': '1677463697059'}, 'messageAttributes': {}, 'md5OfBody': '30de55be8baaf8d8ce6cd51836856f99', 'eventSource': 'aws:sqs', 'eventSourceARN': 'arn:aws:sqs:us-east-1:669676830092:sqsQueue', 'awsRegion': 'us-east-1'}]}

# record = {
#     'Records': [
#         {
#             'messageId': '6ce49fd0-c169-44e7-909f-3b0ad35b9252',
#             'receiptHandle': 'AQEBNWki4Z9tjOXHxZUUyamDphWYaMlZNRN22ta826nyTOGa7OpODvf6F9xFfJOnIqB1x5bf22KrdE5OPsEcZwcimDlKzNr0DLndxA+858vGliDhvNGG+wbmRfZ75uqfjXkmQ/bW4JuJuBsB/ajsviI2fZJPA+ZMMYFLxaso8MLRz5GSF9Zf/vjp371sm/1bzZPS3Qfp1M193KWaEDxuGmW8JYKVRP5h39JyH6VwZNdI1Gc5BObMYqWud94kvezv5C5hrx7JHw5h9hfxu2JzFEOQCUzOdL7tDBCiKFOKyPxiMbbxuVJ3DzUxIJYsPe7uZ0fop2C59d8TYli5/07Ez4zaCVQLJwt/yiPaNN59NDKQBMpHtF9lk8VpqZiUPJaXLjjw',
#             'body': ' {\n    "contrato": [\n        {\n            "NumContrato": "1221112232",\n            "Serie": 22,\n            "id": "1223",\n            "dataContratacao": "10-10-2022"\n        },\n        {\n            "NumContrato": "22222222",\n            "Serie": 33,\n            "id": "2312",\n            "dataContratacao": "15-01-2022"\n        }\n    ],\n    "parcela": [\n        {\n            "NumContrato": "1221112232",\n            "Parcela": 22,\n            "qtdParcela": "320"\n        },\n        {\n            "NumContrato": "22222222",\n            "Parcela": 23,\n            "qtdParcela": "320"\n        }\n    ],\n    "md5": "320"\n}',
#             'attributes': {
#                 'ApproximateReceiveCount': '1',
#                 'SentTimestamp': '1677463697045',
#                 'SenderId': '669676830092',
#                 'ApproximateFirstReceiveTimestamp': '1677463697059'
#             },
#             'messageAttributes': {},
#             'md5OfBody': '30de55be8baaf8d8ce6cd51836856f99',
#             'eventSource': 'aws:sqs',
#             'eventSourceARN': 'arn:aws:sqs:us-east-1:669676830092:sqsQueue',
#             'awsRegion': 'us-east-1'}]}






lambda_handler(record, "Null")
