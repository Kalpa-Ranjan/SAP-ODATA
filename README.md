



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFG62J4Q%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T135117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGOIVNtM2hp68a8v%2Fmhi2HaX9QFDJGHp2JkeW5olzukgIhAJmfmgS74%2B3IC1OIhP4YQFH%2BH%2FXVyM90e9u8lNqiaODKKogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx39gqxxMLWyR4nxEIq3AMg7A7t0hbysz5J%2FwZe47L6lfxwDVzKdUToWNVQCljc4%2F0lb5PsLrwhQBZgjg6X%2FUUZTIFwY6utJDykJX85y5EGDUAhf9S%2BC9LF25UrE5s%2BpqRkl6G9aWZKHbTRaPnR2z8Atju7imGP7SgFf5X5BYxsh49XMzVmHvOPR0TjEtskI%2BEZ3vwsxEvujUVuTrWb3p%2B50R8vGpXlzs6BwVtGm2tvtLLtJFmNMqtCCsI9XaM9s%2FnWer8q%2B41rL06P9ECtaSEghvY1Fe8MDSMNZ0IC8skp624kw2oooBy9L5M9wVpnuXxQB8aGkIcb%2BYiMRFZ%2ByS5NUpqkmlur2CZe7ePC%2F3uehZwO8Rm2zz7evJyl0XQnQbq1S86SLDuum2sPZQbO49vujXqdiXQYqxZzU2FguLKxZkPxaNHVEDjO9JiUzwTUY9mcSTg7IaTAdWuwA7cyUqtc4N2MN7c9G4O8EN%2BeJ7X6V3JzlZ6Y4rtArtzWUFIWT6nJG6m1oD435qmAIUKe5%2FO3MKjT8HEMS1Ow06NCn43kBVT61TllEeoS7ptvr%2FArNiFvLRbTcX4C8srFCVJprlMFjfzALjL5FZWFRvHCjXAluDxVBYFAJJoNzG27dFbNKW3wBUSIpQG9Kzye3zDNyrLTBjqkAWfAQFrtL2nxiuhBPxwnJpHfKY9JlCr8vKkqKOJBHZK2nCtUlkyvfZHZrScoddz6lT6jpt6bHa3fthZzXMG8jbhiXHLSFpzxGr0aa6q%2FPGCACKLEWURwUZenVz0T0%2Brg3qkSEwG5gYlaiJ6J7bL3A8Id9mqTNkyWcHwu4hd2T%2F8BhsEaPZltooV67FzUPMoI27NIlZqSP3VrEAcbV2K4eLChUh8u&X-Amz-Signature=b2edc4bb908a49cca79f55c2f8d8b6271b4889039773a9810a29e435e573f4c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFG62J4Q%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T135117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGOIVNtM2hp68a8v%2Fmhi2HaX9QFDJGHp2JkeW5olzukgIhAJmfmgS74%2B3IC1OIhP4YQFH%2BH%2FXVyM90e9u8lNqiaODKKogECK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx39gqxxMLWyR4nxEIq3AMg7A7t0hbysz5J%2FwZe47L6lfxwDVzKdUToWNVQCljc4%2F0lb5PsLrwhQBZgjg6X%2FUUZTIFwY6utJDykJX85y5EGDUAhf9S%2BC9LF25UrE5s%2BpqRkl6G9aWZKHbTRaPnR2z8Atju7imGP7SgFf5X5BYxsh49XMzVmHvOPR0TjEtskI%2BEZ3vwsxEvujUVuTrWb3p%2B50R8vGpXlzs6BwVtGm2tvtLLtJFmNMqtCCsI9XaM9s%2FnWer8q%2B41rL06P9ECtaSEghvY1Fe8MDSMNZ0IC8skp624kw2oooBy9L5M9wVpnuXxQB8aGkIcb%2BYiMRFZ%2ByS5NUpqkmlur2CZe7ePC%2F3uehZwO8Rm2zz7evJyl0XQnQbq1S86SLDuum2sPZQbO49vujXqdiXQYqxZzU2FguLKxZkPxaNHVEDjO9JiUzwTUY9mcSTg7IaTAdWuwA7cyUqtc4N2MN7c9G4O8EN%2BeJ7X6V3JzlZ6Y4rtArtzWUFIWT6nJG6m1oD435qmAIUKe5%2FO3MKjT8HEMS1Ow06NCn43kBVT61TllEeoS7ptvr%2FArNiFvLRbTcX4C8srFCVJprlMFjfzALjL5FZWFRvHCjXAluDxVBYFAJJoNzG27dFbNKW3wBUSIpQG9Kzye3zDNyrLTBjqkAWfAQFrtL2nxiuhBPxwnJpHfKY9JlCr8vKkqKOJBHZK2nCtUlkyvfZHZrScoddz6lT6jpt6bHa3fthZzXMG8jbhiXHLSFpzxGr0aa6q%2FPGCACKLEWURwUZenVz0T0%2Brg3qkSEwG5gYlaiJ6J7bL3A8Id9mqTNkyWcHwu4hd2T%2F8BhsEaPZltooV67FzUPMoI27NIlZqSP3VrEAcbV2K4eLChUh8u&X-Amz-Signature=b01c0cc4134ad2e60f5fe68b155cbdcdd9e4adb4cf6c1f30b056112d10dbdf16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







