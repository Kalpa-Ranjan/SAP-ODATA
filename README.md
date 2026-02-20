



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JG2AOSV%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T183901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICI5hAqgHcjhX2tiesH9kfsYCp8LYOBQtfgXW%2FnRXRWGAiEAhVcytY6BCV9fRrO8MSOa8iOLTFPJBlvx%2BmW4Cdy67PwqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP%2FVSvu0NUb5JZ2IhircA9jwJwCYxRtMZTJJt80qWJYoc8pP5kSgLShyugwGc4mFA7ux69sWHWFer6jSZPmq3eJv%2B%2F3ivkTNSSl9YJh9rOFyWofGJTbU1jSaJ%2Fswsfcn5lPVo2quKdrRoIS%2B4Pj%2FKVZONWhhyMWMF8TuKpYnqfEDvojHJF2ZkY3u%2FFsu3uL6x5uA4Lp7%2FAha9cHB7h2Bm071A2Oc8I%2BumDhDqo7A8Fsx%2F857VdYAl5JTbCilgg4cB%2BtJL1rMAvFCobnq5Cmnf88omhSPtpVGyHj2Nb4lLYadLgXtEG1GPqcUaiW6FHW%2BI7DF6ci64Q6WGrchV%2BnKzv7vJhMNXDEijTNFBxStD6LJ7LteR1GFCAvUnZIbxi97diKlQRkRhGWD%2BFTRQVfMvqrEM%2BQGYAmd1rvDAN2Gb38fzJ%2F0%2Bi%2FyTXH9%2BvuJPsbEPFJvfqmTB9648PxyFdIFBv2Nh78YoIS2yR5qpf6rz0FiFjZVfWUFb6onK6FhGHh5xBDwm1v4gnvP%2Bn%2FXDeoQCydq6HTAFcML5frsa6I0piBC6FusXJeAT4CAf5T0irmk2L2TaTtURdKDFpcquNuRreYPPEH3EYrBasMLP5J5imzb0Vh8U2ogUclJTGq5UUFsZZKurYrvu0KmVOzzMPCc4swGOqUBsOuOH8AhNbsDWSK8qMk%2BCBCPPdpRIfd7Jm5L6U9xV3M5PwRMrRVM7K5Fymfuw%2FXmwXlr1eUg4MmaHpgsH3gGuOh2s6sqXIfw8vT9UxSUCNzpgKKbg%2FVTlAtMrT8dvRP%2FJ5ZsI%2FxwObZO6kZf8qTCUkBuDoWIrMKfEfHz3Q4VI62yJir9wrnSB6kflRm3K9yOy9Pm%2FZ1CcuHwjLpIAdPoKLNMk4AU&X-Amz-Signature=1b604d0912539eaf1e9bf599a172bff9e245ab9c1d3ba988b5709f0b27beae19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JG2AOSV%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T183901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICI5hAqgHcjhX2tiesH9kfsYCp8LYOBQtfgXW%2FnRXRWGAiEAhVcytY6BCV9fRrO8MSOa8iOLTFPJBlvx%2BmW4Cdy67PwqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP%2FVSvu0NUb5JZ2IhircA9jwJwCYxRtMZTJJt80qWJYoc8pP5kSgLShyugwGc4mFA7ux69sWHWFer6jSZPmq3eJv%2B%2F3ivkTNSSl9YJh9rOFyWofGJTbU1jSaJ%2Fswsfcn5lPVo2quKdrRoIS%2B4Pj%2FKVZONWhhyMWMF8TuKpYnqfEDvojHJF2ZkY3u%2FFsu3uL6x5uA4Lp7%2FAha9cHB7h2Bm071A2Oc8I%2BumDhDqo7A8Fsx%2F857VdYAl5JTbCilgg4cB%2BtJL1rMAvFCobnq5Cmnf88omhSPtpVGyHj2Nb4lLYadLgXtEG1GPqcUaiW6FHW%2BI7DF6ci64Q6WGrchV%2BnKzv7vJhMNXDEijTNFBxStD6LJ7LteR1GFCAvUnZIbxi97diKlQRkRhGWD%2BFTRQVfMvqrEM%2BQGYAmd1rvDAN2Gb38fzJ%2F0%2Bi%2FyTXH9%2BvuJPsbEPFJvfqmTB9648PxyFdIFBv2Nh78YoIS2yR5qpf6rz0FiFjZVfWUFb6onK6FhGHh5xBDwm1v4gnvP%2Bn%2FXDeoQCydq6HTAFcML5frsa6I0piBC6FusXJeAT4CAf5T0irmk2L2TaTtURdKDFpcquNuRreYPPEH3EYrBasMLP5J5imzb0Vh8U2ogUclJTGq5UUFsZZKurYrvu0KmVOzzMPCc4swGOqUBsOuOH8AhNbsDWSK8qMk%2BCBCPPdpRIfd7Jm5L6U9xV3M5PwRMrRVM7K5Fymfuw%2FXmwXlr1eUg4MmaHpgsH3gGuOh2s6sqXIfw8vT9UxSUCNzpgKKbg%2FVTlAtMrT8dvRP%2FJ5ZsI%2FxwObZO6kZf8qTCUkBuDoWIrMKfEfHz3Q4VI62yJir9wrnSB6kflRm3K9yOy9Pm%2FZ1CcuHwjLpIAdPoKLNMk4AU&X-Amz-Signature=0295fae6f79413ccde866c77837026c7acfa958c11482c8b03a7ee56adf81443&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







