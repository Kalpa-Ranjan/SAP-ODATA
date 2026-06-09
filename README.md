



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOWJK2Z2%2F20260609%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260609T024012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZE3Yada4C9hPmGXKE8XAvMQr6QDSsPdFdQ4zffypkKwIhAK4l%2BYnHv59pajDE3X9z9FcwInJEznXizN%2FsTwsexwFvKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyiXlSkuk19PXr0lCQq3APiwe7ZCLI2%2FAVOIXWXXBKX0eARDpAPonunpHq%2BqVPUsGlLc1tiw96kD8J9C9%2F0XyCsM5uFGixy85tsrDi84coUYFfdcGB1U2e5g5PN4emH6bEdceuGWiVBOPX3KMV3DHFStteQijlPvE66OiF7p5gCLTohO4388VL%2FGYxk6PzaOaF55JnAumJQL6uDs%2FQnRxdLwsZIOV%2BO461Pfj2xFhJFBy2yAZ1ldHv8s8qHXRrGqmoCGGYfrp5P2aDP1VHIMBNDAStogEsXH90i%2FCtwn0zZvQjzXBbcu9H4VwLJS3qu0WTWEB1I35agFzCWixJsWV6O1DEWX3weDYP8jr%2BwLCzcVtCActJom0AWi5PD8ztVsYvIuM8uVOGfsjhAp3XY5DfDHpI84%2F2RmsBRU6MR0j8jlDg7KaqFwJZrbiKHa%2BKeGDDmwUXCEDlo5KcLFlLWztbdUZIccWb4MlEcKWMKDKGsmGpbKhdsotvsxu8N2LLXlTHtU6QPZ5S1jDJ1DUTn0U7gel8zEUNGh0MD7%2F138cCfdfbAfInhXXGYnmR94Y18hYCp0%2BYv7J2bc86lHLQev0TmLndZ5E0jTvzLvkiouEUsw8t4ssbAs%2BfhQPQv%2F0tf%2FUtvnVB8yYkMCElQuDCN2J3RBjqkAXzeTBACLNvpBbjCrvep3lzsgmgRSVABLVJH0i4f7xEJx8Mz5HD5MclMHlcrYZPd654i8Htgh3aOkhHwvr6l9IFGk%2Byd2yzOKYpKiUp0TYcBYtIltanML5gtYTr7XyfuldrEiG%2FyfLtqV7WKHDbcMQ%2BWFmwHOUcDYg8FO0ixQHxCSEG2DFQp1jIodNPokV7jc65zA0ESsQeWnN1Uk2vGQ2eRfkJH&X-Amz-Signature=c74959ea66e2c99b5451695fc5a6bf727d557e5ba15cb46712c7d46f4b699ea4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOWJK2Z2%2F20260609%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260609T024012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZE3Yada4C9hPmGXKE8XAvMQr6QDSsPdFdQ4zffypkKwIhAK4l%2BYnHv59pajDE3X9z9FcwInJEznXizN%2FsTwsexwFvKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyiXlSkuk19PXr0lCQq3APiwe7ZCLI2%2FAVOIXWXXBKX0eARDpAPonunpHq%2BqVPUsGlLc1tiw96kD8J9C9%2F0XyCsM5uFGixy85tsrDi84coUYFfdcGB1U2e5g5PN4emH6bEdceuGWiVBOPX3KMV3DHFStteQijlPvE66OiF7p5gCLTohO4388VL%2FGYxk6PzaOaF55JnAumJQL6uDs%2FQnRxdLwsZIOV%2BO461Pfj2xFhJFBy2yAZ1ldHv8s8qHXRrGqmoCGGYfrp5P2aDP1VHIMBNDAStogEsXH90i%2FCtwn0zZvQjzXBbcu9H4VwLJS3qu0WTWEB1I35agFzCWixJsWV6O1DEWX3weDYP8jr%2BwLCzcVtCActJom0AWi5PD8ztVsYvIuM8uVOGfsjhAp3XY5DfDHpI84%2F2RmsBRU6MR0j8jlDg7KaqFwJZrbiKHa%2BKeGDDmwUXCEDlo5KcLFlLWztbdUZIccWb4MlEcKWMKDKGsmGpbKhdsotvsxu8N2LLXlTHtU6QPZ5S1jDJ1DUTn0U7gel8zEUNGh0MD7%2F138cCfdfbAfInhXXGYnmR94Y18hYCp0%2BYv7J2bc86lHLQev0TmLndZ5E0jTvzLvkiouEUsw8t4ssbAs%2BfhQPQv%2F0tf%2FUtvnVB8yYkMCElQuDCN2J3RBjqkAXzeTBACLNvpBbjCrvep3lzsgmgRSVABLVJH0i4f7xEJx8Mz5HD5MclMHlcrYZPd654i8Htgh3aOkhHwvr6l9IFGk%2Byd2yzOKYpKiUp0TYcBYtIltanML5gtYTr7XyfuldrEiG%2FyfLtqV7WKHDbcMQ%2BWFmwHOUcDYg8FO0ixQHxCSEG2DFQp1jIodNPokV7jc65zA0ESsQeWnN1Uk2vGQ2eRfkJH&X-Amz-Signature=dc1bf475e4ab5cfc78d927fc0ea7d8365a73508bcc987c0876efb850847786e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







