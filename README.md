



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVEHQNF3%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T092430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICvE5si%2BNRlLkL0yN9%2FixRq0Pqn5O7bsFWNQ0vEbvrFdAiEAjidntFuywzVXcyUEAxaer6lz3sByQeNnwHtAJL3qG38qiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOTuNzt8NS7mqCCCMCrcA%2B7noENjN3hnF%2Bm3g822BgMe4F6z1eNH7qSRrid0j5BKL2%2F5eT9FP85ntBRmH0iwWZurXFFxqkJAzH9VCx2SkC2I1jdvYjf7semaa0HzvoJyQFHdK8FNoCsRFDfp7yA4vmODg2zhsKpiKWJTd3SMJl5VwrSJTUE7oeJq7%2Bu7g6YHBVexGaXDZN492TdmKply71DFJJ%2BNRA1ryAG44OykGfSVdjlWjL%2BvDV2oQqmf9W2E9L%2BI7NNyrXY7lxf1MDVKAceJPtje67r%2BdOXzYkPdD8YNARHxPOuqPPA1XW7JeUWSCIP8xKR9DHWSCD1VQ2I5UtEwZrufNoJN5thYG%2B2EisHiLBRfYG77oeTPzCfl%2BSLriJrUN68Tcgb3A%2FPIGF37uAxFj5wSLOkL22w78NeQvxAPw%2B3qhFg1ZeD9rURlt6I%2B5Uf8cGNbzTM0lD424Yw2gq8QflPQzMWCsIrBY5ibp53MW3R%2BMiw9rIRSuW6OgUTP07rXs3FsliBSj%2B6wMdl5PvfICELnfEXbLX3H7EP3Ti4acjGpmhQ6e55bVDA2sSmCDL9ZKow2mNuMyJmVh1YMy4TBXaraOd6Pbn5sJ6i7rG9MQ68zSnokGUAVf5l2X%2Btw4bH4TooukjHPrSbKMIuVjtIGOqUBiH%2FYvrGq6G2Llp6jSD4JhysjK5OgEv2q9A6iR6TWgj6MEN%2BhJugWQcoLxMD8D8SGetOMYFfLy3S7BnPj78mtfupjuQOdgJL08FI57EgGlBxE%2FAdrefQEZNNzof9KsHMNQde8G0DHhUbmMHvwaBcchNeXZmmsTyDhXMIGCLBoykh0t5ktN%2Bifq0CxVQHRB%2Bm5JTyD%2Bl5C5B4UFB5VFI1wCMFGkPn7&X-Amz-Signature=7a89d7c5d7d553775fb993a573d014ac4acd3cf4f1c08cdabb9e158a09c7ffce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVEHQNF3%2F20260630%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260630T092430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICvE5si%2BNRlLkL0yN9%2FixRq0Pqn5O7bsFWNQ0vEbvrFdAiEAjidntFuywzVXcyUEAxaer6lz3sByQeNnwHtAJL3qG38qiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOTuNzt8NS7mqCCCMCrcA%2B7noENjN3hnF%2Bm3g822BgMe4F6z1eNH7qSRrid0j5BKL2%2F5eT9FP85ntBRmH0iwWZurXFFxqkJAzH9VCx2SkC2I1jdvYjf7semaa0HzvoJyQFHdK8FNoCsRFDfp7yA4vmODg2zhsKpiKWJTd3SMJl5VwrSJTUE7oeJq7%2Bu7g6YHBVexGaXDZN492TdmKply71DFJJ%2BNRA1ryAG44OykGfSVdjlWjL%2BvDV2oQqmf9W2E9L%2BI7NNyrXY7lxf1MDVKAceJPtje67r%2BdOXzYkPdD8YNARHxPOuqPPA1XW7JeUWSCIP8xKR9DHWSCD1VQ2I5UtEwZrufNoJN5thYG%2B2EisHiLBRfYG77oeTPzCfl%2BSLriJrUN68Tcgb3A%2FPIGF37uAxFj5wSLOkL22w78NeQvxAPw%2B3qhFg1ZeD9rURlt6I%2B5Uf8cGNbzTM0lD424Yw2gq8QflPQzMWCsIrBY5ibp53MW3R%2BMiw9rIRSuW6OgUTP07rXs3FsliBSj%2B6wMdl5PvfICELnfEXbLX3H7EP3Ti4acjGpmhQ6e55bVDA2sSmCDL9ZKow2mNuMyJmVh1YMy4TBXaraOd6Pbn5sJ6i7rG9MQ68zSnokGUAVf5l2X%2Btw4bH4TooukjHPrSbKMIuVjtIGOqUBiH%2FYvrGq6G2Llp6jSD4JhysjK5OgEv2q9A6iR6TWgj6MEN%2BhJugWQcoLxMD8D8SGetOMYFfLy3S7BnPj78mtfupjuQOdgJL08FI57EgGlBxE%2FAdrefQEZNNzof9KsHMNQde8G0DHhUbmMHvwaBcchNeXZmmsTyDhXMIGCLBoykh0t5ktN%2Bifq0CxVQHRB%2Bm5JTyD%2Bl5C5B4UFB5VFI1wCMFGkPn7&X-Amz-Signature=9ad00e63af85d8c51f3aeff552b84c7ca77e2f25992264e3dd59a577384fc187&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







