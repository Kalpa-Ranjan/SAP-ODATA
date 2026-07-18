



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TEH7636%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T074010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpUZEGjCfdOcC48JqIN1ykdw8E7y4fRpzuUMQdKm66lgIgCZruGGFUuAfKUJBRpV8PfkWyYgbFX%2F4XgDIIUIKDRjMq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDCAtnnigaiohHwaE1CrcA7UQRFkrKrPuB3nfb1dhWYlM44qblBdt5j3ZKbkdsmgGXWVpILVwVCJO7QV42yViL4iaYcUZVFKN1Uatd%2BkiGUmKNDBI7h62BCErvH5bkWMjvpmxqvPHpkJlR2Lb52R4QC49dyRTbmLS8PKRK6Qnb4Eu1k1W0Gov4nmgNg%2BqW22sYQgXPTkqNi9X6ssSwYk4PH9GfC6KmUwVhcsOjkggSxqfjc8OAhX3tuNlK5AVg3Iq3PADcjCwc%2BPeqtBCGd8fhidJz2yMsWaisYUiqWntvXSrhUP%2B0c4C5xKk4CM4MTHSmZ1ohpBe4VhuVLLoQVaqpVftguNNfyJalLKKfR3RbKenikl5BLpIbX6xvi6P0hdjfvHTqWahfpMgGwVX8UWhj62vaw6rBqvJNYai0E6iiDVR5oaitxtYLDWGifJwWR%2Btl5FWlyrZqDlGxjOiqBnaCuVd9wzjKtaWizV29HOk5zKu2k0FXX%2FyZOQTbd03pV7t1cCgznvd6BaDTX6iu2npV2bynhtDuWHbuq2liEMUqdHO5UUksq32f1tW4DOo%2BW1rWU5MtM0K0nPcpF6HZm5%2BrVSEL1YNeZrCwt%2BQXg0zH80JBTZLEPn0pF3ftmUoreKqJ7J%2B1YJBGnQ2eLR0MNzB7NIGOqUBEfhG7kbyGy%2BFpeIz%2FVpjsTgs0TWleoSkHPF8f%2BioH4nY2B4PlfHbHpqT7qK%2B6ZpT6N2Lold9Azlh6byNysElUfvl%2FTOXEBwrOm1XzqIAJ4Jgj5WwZcI9lJlAkzQUdvW6%2B5DxDPDwG1pqr%2BFvGsGaL5CKyQP2md%2BLDh8e2CvgyfadVsSfwk34ZaetV2kqmYKQHNgYDFBmkh7rIr2EAgBlv%2B0zyPgb&X-Amz-Signature=d17881e2cb759c1552fe20f97b7f97ac390e064cb2089e2240055c1e2aa2aa17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TEH7636%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T074010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpUZEGjCfdOcC48JqIN1ykdw8E7y4fRpzuUMQdKm66lgIgCZruGGFUuAfKUJBRpV8PfkWyYgbFX%2F4XgDIIUIKDRjMq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDCAtnnigaiohHwaE1CrcA7UQRFkrKrPuB3nfb1dhWYlM44qblBdt5j3ZKbkdsmgGXWVpILVwVCJO7QV42yViL4iaYcUZVFKN1Uatd%2BkiGUmKNDBI7h62BCErvH5bkWMjvpmxqvPHpkJlR2Lb52R4QC49dyRTbmLS8PKRK6Qnb4Eu1k1W0Gov4nmgNg%2BqW22sYQgXPTkqNi9X6ssSwYk4PH9GfC6KmUwVhcsOjkggSxqfjc8OAhX3tuNlK5AVg3Iq3PADcjCwc%2BPeqtBCGd8fhidJz2yMsWaisYUiqWntvXSrhUP%2B0c4C5xKk4CM4MTHSmZ1ohpBe4VhuVLLoQVaqpVftguNNfyJalLKKfR3RbKenikl5BLpIbX6xvi6P0hdjfvHTqWahfpMgGwVX8UWhj62vaw6rBqvJNYai0E6iiDVR5oaitxtYLDWGifJwWR%2Btl5FWlyrZqDlGxjOiqBnaCuVd9wzjKtaWizV29HOk5zKu2k0FXX%2FyZOQTbd03pV7t1cCgznvd6BaDTX6iu2npV2bynhtDuWHbuq2liEMUqdHO5UUksq32f1tW4DOo%2BW1rWU5MtM0K0nPcpF6HZm5%2BrVSEL1YNeZrCwt%2BQXg0zH80JBTZLEPn0pF3ftmUoreKqJ7J%2B1YJBGnQ2eLR0MNzB7NIGOqUBEfhG7kbyGy%2BFpeIz%2FVpjsTgs0TWleoSkHPF8f%2BioH4nY2B4PlfHbHpqT7qK%2B6ZpT6N2Lold9Azlh6byNysElUfvl%2FTOXEBwrOm1XzqIAJ4Jgj5WwZcI9lJlAkzQUdvW6%2B5DxDPDwG1pqr%2BFvGsGaL5CKyQP2md%2BLDh8e2CvgyfadVsSfwk34ZaetV2kqmYKQHNgYDFBmkh7rIr2EAgBlv%2B0zyPgb&X-Amz-Signature=ea0d6971d855eed150e9b49d2c3e8ef455269f8f521f367a8d680fc987d0abaf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







