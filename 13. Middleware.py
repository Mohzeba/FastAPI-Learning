from fastapi import FastAPI, Request
import time

app = FastAPI()

# Middleware runs on every request before and after it hits the endpoint
@app.middleware("http")
async def log_middleware(request: Request, call_next):
    
    # Record the time when request arrives
    start_time = time.time()
    
    # Pass the request to the actual endpoint and wait for response
    response = await call_next(request)
    
    # Calculate how long the request took to process
    process_time = time.time() - start_time
    
    # Print the path and time taken to the terminal (for logging/debugging)
    print(f"Path:{request.url.path} | Time:{process_time}")
    
    # Return the response back to the client
    return response


#@app.middleware("https")
#async def my_middleware(request : Request,call_next):
#    print("Request Received")
#    response = await call_next(request)
#    print("Response Sent")
#    return response