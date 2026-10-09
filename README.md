



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEGHTZKN%2F20261009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261009T180931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJIMEYCIQDGHAFj7LrjdAmeqHny8Derq2LfUNPfHg5wr4iC7kCmQwIhAMecoK%2Bt3FUVOcfGuNppI2z5VO5QyNQX8E1hHTRk5FDIKv8DCEIQABoMNjM3NDIzMTgzODA1IgxBc98pkznC34Crgmoq3AOhxSiBwwIb2mW03djDhRQbwJL2JPnG%2FKh0wN868Rw%2BdolgeFp3Ll9SsE%2Bv1P%2BE0iDoMlgby2sxj2nF2nRUcZFOPV6cBipiBHC%2BsL1oz%2BWXn6DFxGyPvT3AhV%2FKODijGkniila18Q0qIUfmjwJZOBYQTmvaUncvHDpXI%2FiYZsWDn8jLln9dKdhh4c4Hh4E%2B%2FeSEmZN3GhD3RnaEiC2jmvhAAaZex4QqJTRBGYJCF77Bv7JxVoQiRVTSPSGEv4l5OnaUFUfNds7aBBnfpDrSyRWAGSXtYUnHjhhkRxu9jY83VQ7aaB20WFLBKIAkVB%2Fbrnff7RDHN0x5JrCp2sWuyct3Nhw9Um4pqUXGLRNbOOGIYBatxvo5ycvcufhCtgGC6K4Licijvl%2B9tYCIGDPk%2F%2BT0E8vA8eGfJ15zfS9GuNgAgChQxxh79ncOGpsmNCf0puPT2ksK%2FFCfnKSceqpgKCBCR5LJDNL%2F1EY4qHuXbW8H8cknzH9O1o3fjs3YB3ATSyemh7rm%2BPeg9h1kKMGpg8AoQLb82Q%2BFhXi4rFqfMi%2Fz%2BcwbScZ19wa989Yk0yrTCn%2Fhj%2BrGoFlWI612Wpm9JJEecXhT%2FkcOXjB4%2FKVDyprJz3fmi1ZiBAb5PQfctTC5tKTWBjqkAVvTf2L%2BFsWQGLtIOrRaY1rWJ8kS%2BZqSwU3giogYRcChCF9L8v23MBY130UnTEVz6rgXG59C72dAA%2BdhCai%2FeFfKnsDKUFlt0pHffA7hzAx6VoEHO9RwXc1KnDySwXNBW6McW5W98sN7YmTXIziyCLrbpc1G7VH9sk1EAUdfd4OkiDKsxg%2Foz%2BnQdjA4x7VfYqiBkxfSgDs2Z2H8eH6elEbOOMzF&X-Amz-Signature=31ebbaba6f492489b07f6a9c8e66516ea83da7f298d95cf0d5e65794f9024417&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEGHTZKN%2F20261009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261009T180931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJIMEYCIQDGHAFj7LrjdAmeqHny8Derq2LfUNPfHg5wr4iC7kCmQwIhAMecoK%2Bt3FUVOcfGuNppI2z5VO5QyNQX8E1hHTRk5FDIKv8DCEIQABoMNjM3NDIzMTgzODA1IgxBc98pkznC34Crgmoq3AOhxSiBwwIb2mW03djDhRQbwJL2JPnG%2FKh0wN868Rw%2BdolgeFp3Ll9SsE%2Bv1P%2BE0iDoMlgby2sxj2nF2nRUcZFOPV6cBipiBHC%2BsL1oz%2BWXn6DFxGyPvT3AhV%2FKODijGkniila18Q0qIUfmjwJZOBYQTmvaUncvHDpXI%2FiYZsWDn8jLln9dKdhh4c4Hh4E%2B%2FeSEmZN3GhD3RnaEiC2jmvhAAaZex4QqJTRBGYJCF77Bv7JxVoQiRVTSPSGEv4l5OnaUFUfNds7aBBnfpDrSyRWAGSXtYUnHjhhkRxu9jY83VQ7aaB20WFLBKIAkVB%2Fbrnff7RDHN0x5JrCp2sWuyct3Nhw9Um4pqUXGLRNbOOGIYBatxvo5ycvcufhCtgGC6K4Licijvl%2B9tYCIGDPk%2F%2BT0E8vA8eGfJ15zfS9GuNgAgChQxxh79ncOGpsmNCf0puPT2ksK%2FFCfnKSceqpgKCBCR5LJDNL%2F1EY4qHuXbW8H8cknzH9O1o3fjs3YB3ATSyemh7rm%2BPeg9h1kKMGpg8AoQLb82Q%2BFhXi4rFqfMi%2Fz%2BcwbScZ19wa989Yk0yrTCn%2Fhj%2BrGoFlWI612Wpm9JJEecXhT%2FkcOXjB4%2FKVDyprJz3fmi1ZiBAb5PQfctTC5tKTWBjqkAVvTf2L%2BFsWQGLtIOrRaY1rWJ8kS%2BZqSwU3giogYRcChCF9L8v23MBY130UnTEVz6rgXG59C72dAA%2BdhCai%2FeFfKnsDKUFlt0pHffA7hzAx6VoEHO9RwXc1KnDySwXNBW6McW5W98sN7YmTXIziyCLrbpc1G7VH9sk1EAUdfd4OkiDKsxg%2Foz%2BnQdjA4x7VfYqiBkxfSgDs2Z2H8eH6elEbOOMzF&X-Amz-Signature=22d56466e5a47a7efa8b9c8579ea4c48a02bf7ffd1429b4a293d42ba1f4a5129&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







