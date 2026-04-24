



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SED7N7LZ%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T020904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClfAl8m3TvALg2i5aNGaBHqUl3KMvfEoqZMSylVkAUAQIhAM2aezYnUr03On2lMXnfI5LLp%2Fm0zjK01d0pbHNECd1TKv8DCG4QABoMNjM3NDIzMTgzODA1Igw6rVx6kE9h560EOn8q3ANdnJd3Z211F66TTsrjLUrSPYgeD%2FQAOzW9DcAVA4Cn9jDQyqXaC50saiaGIvDmQuAK1VBrk0kNUkEZsuqcZSlHh01oDEdxkYc6boId2Zwe6OuNnjVDARbuQbijSCh7b589SqgL8v6bChGwPrsvoOqMhVmrlYUXpDhHSgzn%2BLMxspS7y916Kw2%2FRwYHV4c1BpntNqXqSF3nzaSR0%2BzGO%2By0Jga5PbcFMe3zgYywQR0HTXZyN3a7o5ozzI%2BxUEtYEKxz5EdEmr7hxdFSgyYesfE9cU2FJcazvx6PfD%2BGxLm3S8VwFPD%2BW%2F0STLyhpkiQe4XdW8Adf0gPWFm3AWd9faC0Igyq9l5waP0q%2FtJ3aEFsduAci2xTf5htJohhhXiueQjAQfR1oLAssQwFdn18knOEbJy14aUrZ8gVd64aP8xZ3rtNsOrTTz7ogX1d7S%2B2FWnFGfKwPs80P8Ywy1emZfj3VfhU3dOf8uFyWhtYKg%2FnMr%2FNCEWXx5zNNNW1EKAq01qf%2BodeOAEO%2F6b9NdRFKF5qIsR8yjQUn87r75SraApqWZ8RupSiU6XYAoO48Sc5UaU5ORbuIDjI5DMEkluTeGLpHfqyc8HBs9YPFZylnoytEZmdjLZUNNt%2BZVz5sjDji6rPBjqkAcFz%2FbL7TFdekPYQqojalwRZA6SFC3H3gXwW11WVaWthBhpKrpcas7pW5n3UpFgZWwff0fJi7s0Ps5k3hE5y6AWnQMAdzHhoJ8jr1OK294f8YtWvJcn0NwW6y%2F0e91MabH9haO2uzaG9A2ifrtZRcuugW3dEkSXRefpMOckFdjizfIaezveIxbV8FgsP90rDTKkl%2FcKe%2FxZ7XHo5ZbWX%2B7GgIwuQ&X-Amz-Signature=3a40cf25f6ff9a424546b5b3e251877abb260f11278dd928e1d7fd3e2350cb2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SED7N7LZ%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T020905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClfAl8m3TvALg2i5aNGaBHqUl3KMvfEoqZMSylVkAUAQIhAM2aezYnUr03On2lMXnfI5LLp%2Fm0zjK01d0pbHNECd1TKv8DCG4QABoMNjM3NDIzMTgzODA1Igw6rVx6kE9h560EOn8q3ANdnJd3Z211F66TTsrjLUrSPYgeD%2FQAOzW9DcAVA4Cn9jDQyqXaC50saiaGIvDmQuAK1VBrk0kNUkEZsuqcZSlHh01oDEdxkYc6boId2Zwe6OuNnjVDARbuQbijSCh7b589SqgL8v6bChGwPrsvoOqMhVmrlYUXpDhHSgzn%2BLMxspS7y916Kw2%2FRwYHV4c1BpntNqXqSF3nzaSR0%2BzGO%2By0Jga5PbcFMe3zgYywQR0HTXZyN3a7o5ozzI%2BxUEtYEKxz5EdEmr7hxdFSgyYesfE9cU2FJcazvx6PfD%2BGxLm3S8VwFPD%2BW%2F0STLyhpkiQe4XdW8Adf0gPWFm3AWd9faC0Igyq9l5waP0q%2FtJ3aEFsduAci2xTf5htJohhhXiueQjAQfR1oLAssQwFdn18knOEbJy14aUrZ8gVd64aP8xZ3rtNsOrTTz7ogX1d7S%2B2FWnFGfKwPs80P8Ywy1emZfj3VfhU3dOf8uFyWhtYKg%2FnMr%2FNCEWXx5zNNNW1EKAq01qf%2BodeOAEO%2F6b9NdRFKF5qIsR8yjQUn87r75SraApqWZ8RupSiU6XYAoO48Sc5UaU5ORbuIDjI5DMEkluTeGLpHfqyc8HBs9YPFZylnoytEZmdjLZUNNt%2BZVz5sjDji6rPBjqkAcFz%2FbL7TFdekPYQqojalwRZA6SFC3H3gXwW11WVaWthBhpKrpcas7pW5n3UpFgZWwff0fJi7s0Ps5k3hE5y6AWnQMAdzHhoJ8jr1OK294f8YtWvJcn0NwW6y%2F0e91MabH9haO2uzaG9A2ifrtZRcuugW3dEkSXRefpMOckFdjizfIaezveIxbV8FgsP90rDTKkl%2FcKe%2FxZ7XHo5ZbWX%2B7GgIwuQ&X-Amz-Signature=500e857b33143502bd4c0054015f51f637956024694212011b7061bb3b5564bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







