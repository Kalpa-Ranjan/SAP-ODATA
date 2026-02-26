



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656AHYWHT%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T065419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIDWAa%2F%2BW5raRX%2BXilyIfF3l4%2F6wTwgC73AW4GXvaos6bAiEAneb%2BpJ2kOyRffH%2FzI2kA%2B%2BH8dheSTmeINzfQ183mI8Eq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDMtoSUvR%2F0NNAeT47ircA7dMg8CLjf2DOdwP2nabCxWs3FfHYozyVWLinGQItrvl0MqeK0rKlIkwKyVTFWAMao0B8RiarA4HpAbFSVAm8ADB8BK%2FaZnh1ngH4KYnjs5PqbwyOxpNTAJbuUuZHmdXVEC0lpduNTfS72NDxpcNibhL65nd%2BvqZpAKCFJI69IwuOPvWYC%2BCACY7m2kcezngIqODQODnCAenGfXxd50m4tvj7f7FkY1NajThorJkzxYT%2BUZ8wm13SjDwcBQVDV186BQd53qPvB%2FCfuVagr9ICfXxHVqU2vP6jrHieucx7eNHneA6hi1XwbpEMm8uL7prjqs%2B1jpTUeJENEAWc979d9x%2B6R%2B04LSMNZkacOdVJot14TKmK57X2STKNDCZMi1nxjlDemL3fXnCxlEp9Hd04z2r4SXGz2E3casrbTHRxbALJ%2FNPXfl6uUfUo4jGpv1fMUFrqu3fy1hAmZXTxK39znahxhZR0z8uwle46JjtBrSCq6r3tAWx7kR%2BecacoDzONnKJZMOadgA9GLoO9Rz58TmblM1bqp1FPM0GvNEJWNc9qR4ZadNiRKLlDJM3mLDjGJlbHfFOakCbYsR0mwMcUk3tqtSaErP9%2FI%2B6CZolp%2FyBi%2B9euENWOUQm3F5rMMSY%2F8wGOqUBz%2Fdgx1LwWnQwW46tVmePmZ1KONpjxQuX5gBA6ueu1r7B2zgUZSPSUo5VmtA9ypWF%2FbvgtrwmwNVTya8mJMOPhjCvDDKdapopdPfW4e02XAiHiJppYMPD5FjDeFlDecBbC%2Fixdj6%2Fxk%2FPgy%2F8iZSAmm2YUfW2KSeYDWtYAxw%2BX%2Fo9lQLPmqveeWMIZaUcBnuzbRNBMkSmU3Gfxc3OIDhMArhDprWf&X-Amz-Signature=3d34f25c512c406046af44107a7785e1180d830638596f4d8490276914e09df0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656AHYWHT%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T065419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIDWAa%2F%2BW5raRX%2BXilyIfF3l4%2F6wTwgC73AW4GXvaos6bAiEAneb%2BpJ2kOyRffH%2FzI2kA%2B%2BH8dheSTmeINzfQ183mI8Eq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDMtoSUvR%2F0NNAeT47ircA7dMg8CLjf2DOdwP2nabCxWs3FfHYozyVWLinGQItrvl0MqeK0rKlIkwKyVTFWAMao0B8RiarA4HpAbFSVAm8ADB8BK%2FaZnh1ngH4KYnjs5PqbwyOxpNTAJbuUuZHmdXVEC0lpduNTfS72NDxpcNibhL65nd%2BvqZpAKCFJI69IwuOPvWYC%2BCACY7m2kcezngIqODQODnCAenGfXxd50m4tvj7f7FkY1NajThorJkzxYT%2BUZ8wm13SjDwcBQVDV186BQd53qPvB%2FCfuVagr9ICfXxHVqU2vP6jrHieucx7eNHneA6hi1XwbpEMm8uL7prjqs%2B1jpTUeJENEAWc979d9x%2B6R%2B04LSMNZkacOdVJot14TKmK57X2STKNDCZMi1nxjlDemL3fXnCxlEp9Hd04z2r4SXGz2E3casrbTHRxbALJ%2FNPXfl6uUfUo4jGpv1fMUFrqu3fy1hAmZXTxK39znahxhZR0z8uwle46JjtBrSCq6r3tAWx7kR%2BecacoDzONnKJZMOadgA9GLoO9Rz58TmblM1bqp1FPM0GvNEJWNc9qR4ZadNiRKLlDJM3mLDjGJlbHfFOakCbYsR0mwMcUk3tqtSaErP9%2FI%2B6CZolp%2FyBi%2B9euENWOUQm3F5rMMSY%2F8wGOqUBz%2Fdgx1LwWnQwW46tVmePmZ1KONpjxQuX5gBA6ueu1r7B2zgUZSPSUo5VmtA9ypWF%2FbvgtrwmwNVTya8mJMOPhjCvDDKdapopdPfW4e02XAiHiJppYMPD5FjDeFlDecBbC%2Fixdj6%2Fxk%2FPgy%2F8iZSAmm2YUfW2KSeYDWtYAxw%2BX%2Fo9lQLPmqveeWMIZaUcBnuzbRNBMkSmU3Gfxc3OIDhMArhDprWf&X-Amz-Signature=f798d9fd487e0fab24f6a481e66250f35e0d0d9f8b0f51b86350fc4aafdb45c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







