# Match case works like ifelse statements if it finds the exact value it return or it moves to another case

def http_status(status:int):
    match status:
        case 200:
            return "OK"
        case 400:
            return "Bad Request"
        case 401:
            return "Unauthorised"
        case 404:
            return "Not Found"
        case 429:
            return "Too Many Requests"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
        
print(http_status(200))
print(http_status(429))
print(http_status(29378))