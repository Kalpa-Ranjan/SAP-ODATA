



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    1. RPC APIs:- Remote Procedure Calls
    1. WebSocket APIs:- Used JSON objects, two way communication
    1. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    1. The formatted resource is called a Representation in REST.
    1. Request should identify recourses by using URI
    1. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    1. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    1. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    1. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKTYUKOY%2F20251030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251030T230359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIGWDYXPi4%2Bn6yv%2BIvCF7ymLCVtlJoDLEY8h3o8Z9u9mYAiAVZZwajTZZ15l9TSbg%2BQLbxz3M5Uglxa4dgXufKdRXdyqIBAj3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMOo%2FpWmWWVIMXGa%2FKtwD%2Brg5L0NjQHOi2ISj5x%2FPSAtBUDbI7wlzTw3OFNHkNVBVjbtYykL%2F0akOHkA%2FAMAVOZ6q8DKKMgWrWC5VM8L6%2F46z0%2BZyhUjKN6TxaNXPvw7s%2BwUtZ7gFzKpTVJt5X4cR8aHZ171HQERthVp0rebtWVhpKhNTkll6IvgNVPl1kAtVC1vWRHC9TjFuAiJULM6AF0NKCP1TSEtHef8yPu%2BZX1IOuRm9d4M6N39%2Be0tyKaKPFGay63%2F46LCU5Z1XtzdwwJvtyf59iSldrb%2FYSXPSf4W3PdrhbbWFCjnQ2EsvAs94iqv1IYr8%2FQ1JpQbVxj9CCIYRQPLf6V9%2F2KZw9PdNPQ6db0pzm8gL7E1k6RRSgRWdGGY0ytZy4N7Tb4Loex%2F0fr7N6VmSCcA3Ud7n%2FP6qqqX7l6a5OhtEbwrsNj3S0GM5iEomwUow%2BvLT1An4O%2BpqmoanXkyzy0XrdIqQp78jRhr7LDM1x%2FXvbZDTouNoCo1D63EnPxI32MtkruopTwHxiTssbkG0glkxedssI387VaxMhD9U7Fza%2BwbkHBm7GRiyGMu8tvwJs43feBTarwsBZW19wKOilVlrGgbgTm7m7pO3eyi21%2BEiYNyLPpSR0zNqhS6sY6tcQNDFV1YwlcaPyAY6pgEB85%2BZKEfdUziCP%2F2M102WMAetNUSymUQPm%2FRa0DGx%2FE0bkBHw2RRNt46wfLq8p3hzbn3bPowaWS8Hieh45N1eN6zQ59hIqleGC3YRsxhUvuE9SpiSEG22v2EV1Kd9DHiww1iVEgzEyGTU4uzsGHThS348AxWCukhOzdAO2oUu7oZ%2Fes56dB9q%2BCZf%2F4X6V5pvOoMW4NVJ9khmxKpdoKslKrc08AOY&X-Amz-Signature=e29ccce024954be59dfe398b5971dad86a47e17d6290d03369a39ccdfd1ad009&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKTYUKOY%2F20251030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251030T230359Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIGWDYXPi4%2Bn6yv%2BIvCF7ymLCVtlJoDLEY8h3o8Z9u9mYAiAVZZwajTZZ15l9TSbg%2BQLbxz3M5Uglxa4dgXufKdRXdyqIBAj3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMOo%2FpWmWWVIMXGa%2FKtwD%2Brg5L0NjQHOi2ISj5x%2FPSAtBUDbI7wlzTw3OFNHkNVBVjbtYykL%2F0akOHkA%2FAMAVOZ6q8DKKMgWrWC5VM8L6%2F46z0%2BZyhUjKN6TxaNXPvw7s%2BwUtZ7gFzKpTVJt5X4cR8aHZ171HQERthVp0rebtWVhpKhNTkll6IvgNVPl1kAtVC1vWRHC9TjFuAiJULM6AF0NKCP1TSEtHef8yPu%2BZX1IOuRm9d4M6N39%2Be0tyKaKPFGay63%2F46LCU5Z1XtzdwwJvtyf59iSldrb%2FYSXPSf4W3PdrhbbWFCjnQ2EsvAs94iqv1IYr8%2FQ1JpQbVxj9CCIYRQPLf6V9%2F2KZw9PdNPQ6db0pzm8gL7E1k6RRSgRWdGGY0ytZy4N7Tb4Loex%2F0fr7N6VmSCcA3Ud7n%2FP6qqqX7l6a5OhtEbwrsNj3S0GM5iEomwUow%2BvLT1An4O%2BpqmoanXkyzy0XrdIqQp78jRhr7LDM1x%2FXvbZDTouNoCo1D63EnPxI32MtkruopTwHxiTssbkG0glkxedssI387VaxMhD9U7Fza%2BwbkHBm7GRiyGMu8tvwJs43feBTarwsBZW19wKOilVlrGgbgTm7m7pO3eyi21%2BEiYNyLPpSR0zNqhS6sY6tcQNDFV1YwlcaPyAY6pgEB85%2BZKEfdUziCP%2F2M102WMAetNUSymUQPm%2FRa0DGx%2FE0bkBHw2RRNt46wfLq8p3hzbn3bPowaWS8Hieh45N1eN6zQ59hIqleGC3YRsxhUvuE9SpiSEG22v2EV1Kd9DHiww1iVEgzEyGTU4uzsGHThS348AxWCukhOzdAO2oUu7oZ%2Fes56dB9q%2BCZf%2F4X6V5pvOoMW4NVJ9khmxKpdoKslKrc08AOY&X-Amz-Signature=b5602d46a0330f8d45b6f40011b7e4fbbb1e59e5ed9e9c2b8ba24c5e68f69eb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  1. Atom publishing Protocol
  1. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Test Github-Notion synch



