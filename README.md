



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

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

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW2G5KR2%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T182034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIFV0uINM1uvpdcvpQwiUOXnjllQI%2FtXtrwzx7jDVzCt6AiAQl1cFSEzs37NYH8GglvjqsD8v47Nm3VclxheVJ6Hxkyr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMGMjH5yMXRE%2FYxleCKtwD3HLz4HCW9scKKIOoS1ZI0N0pc8BHJ0bW%2FaDcNCBRdQ8CdFZ2k%2FtXUx%2F4Ynkl0wxP8dPexglBV7C1VPlvAzh68CCfnkz%2BJNujHr6eUCxpkWyhykpz5NU8AzUua%2FVxUsKr3tqqc5y%2FWKRWsydyl5LExZR54rnasihSQHPINY%2FoxVZmgjAdFpAATTVdRjoFINwhetoxRpanEq1%2FxUaBFYCsMO78%2B2u3wu5MTLLpqvqTu9D44exnbQ5nrvQZEoJTC8oUTJh%2B08q2blL68mpeJEdyOTmZTXKuXDHfbZ7%2BAoudyGz8f465u7H5yzEWJCxYEI9RjOtwn%2B2tLleSx%2FqdJcejlXRHyB5G8YCLdE3q3ivM%2B5Bbe4qyGWHKvNCr3LgniKUOg4A95rwbbDdwRfxZBEVg34RLjDFSANqEsfJAznCS3ebbOl5MpO3KpKPvXpuDcoWFGYKoZ6sa%2BMG34SH2j%2BiwjBt77uw1l7JwUd%2FpnjXlU210QS1oymvwJnrT62f5S932v8Q9lfrtJlxZl%2FloRyw4J33dzq48vbg%2F0Ec9%2BpnIbFxWRwoeD9FCsFLswBLc%2FSvZEfaKPTTlFzPbUbCFS6KxfxEOcnmKg%2FVsSHvv5m9I2RWG92yKhRRSPy6bSlcwzrz2yQY6pgEInl1nenj4B5GtoT9sfMIE5DQovat1QFL2cS8uQ2igmgHnZXXXF7kdKzTMcUlDhU63ft2WLA0%2FuQY49zVaILlnssEo2P%2B%2FIGg8cJcnj8fYAfVF2ngpnClig4qVbiFUkihKaGkCmKQ%2BBIIw36tRgcDpI6HzTZqnZSxM7xXgUUkiL6ybAfHO5vmJFjtkjHOGbxg1orH%2BGsGN4ZaZMZr%2FAiEhxkmkQa%2Fi&X-Amz-Signature=8d199456d05007f5bd30ffe731849d9d53f214b5f808c17d14590dac49eb3577&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW2G5KR2%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T182034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIFV0uINM1uvpdcvpQwiUOXnjllQI%2FtXtrwzx7jDVzCt6AiAQl1cFSEzs37NYH8GglvjqsD8v47Nm3VclxheVJ6Hxkyr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMGMjH5yMXRE%2FYxleCKtwD3HLz4HCW9scKKIOoS1ZI0N0pc8BHJ0bW%2FaDcNCBRdQ8CdFZ2k%2FtXUx%2F4Ynkl0wxP8dPexglBV7C1VPlvAzh68CCfnkz%2BJNujHr6eUCxpkWyhykpz5NU8AzUua%2FVxUsKr3tqqc5y%2FWKRWsydyl5LExZR54rnasihSQHPINY%2FoxVZmgjAdFpAATTVdRjoFINwhetoxRpanEq1%2FxUaBFYCsMO78%2B2u3wu5MTLLpqvqTu9D44exnbQ5nrvQZEoJTC8oUTJh%2B08q2blL68mpeJEdyOTmZTXKuXDHfbZ7%2BAoudyGz8f465u7H5yzEWJCxYEI9RjOtwn%2B2tLleSx%2FqdJcejlXRHyB5G8YCLdE3q3ivM%2B5Bbe4qyGWHKvNCr3LgniKUOg4A95rwbbDdwRfxZBEVg34RLjDFSANqEsfJAznCS3ebbOl5MpO3KpKPvXpuDcoWFGYKoZ6sa%2BMG34SH2j%2BiwjBt77uw1l7JwUd%2FpnjXlU210QS1oymvwJnrT62f5S932v8Q9lfrtJlxZl%2FloRyw4J33dzq48vbg%2F0Ec9%2BpnIbFxWRwoeD9FCsFLswBLc%2FSvZEfaKPTTlFzPbUbCFS6KxfxEOcnmKg%2FVsSHvv5m9I2RWG92yKhRRSPy6bSlcwzrz2yQY6pgEInl1nenj4B5GtoT9sfMIE5DQovat1QFL2cS8uQ2igmgHnZXXXF7kdKzTMcUlDhU63ft2WLA0%2FuQY49zVaILlnssEo2P%2B%2FIGg8cJcnj8fYAfVF2ngpnClig4qVbiFUkihKaGkCmKQ%2BBIIw36tRgcDpI6HzTZqnZSxM7xXgUUkiL6ybAfHO5vmJFjtkjHOGbxg1orH%2BGsGN4ZaZMZr%2FAiEhxkmkQa%2Fi&X-Amz-Signature=519f6c2bdce35c42e367955243047483bea57076bd9449f76a077ad12284a311&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


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





Final Test







