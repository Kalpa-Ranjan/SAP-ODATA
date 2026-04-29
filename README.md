



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM4KVHKH%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T191711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD1Pkn6VLaj6QMXO8FCJZ4E4%2Fnhcd938YJVxuiv%2FjXRsAIhAIkehf6jp1eCiT0sVWdSbSORSgU%2Bh9r7Kzg4txCWqdBMKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzOlWtEPBrpASDSnhsq3AOEwFWaCZ%2FQgfUWtuT7xLo4Kem35amVCdaTejWXGZn5U1ywnWnrPjdCr5h7A%2BHnIvDbZDzXcXFP%2Bvv9Igymn5DezdF%2B3IbLDiT65cvjOFvr%2B2mHuL7YKEGUT%2FTgcFC29Cr8paRadoEgXYYcsdWZa9d5kN%2F8wlkh0DEH8yN%2FGYUeQV%2BzRn8vxIoX3mc1Sum99wRdQicH7poDGjRMu56vt9qEE4Ic6jA553JjPD6NytHqztO7jEJLRr4BJK5Q82v%2BReShzsssw63GSesxO6MIvshLDfQevmg%2F4yBMw5MdnREzlUyd0GYehYhs2iCk3t97YdswBlRtvVx5XHq40v%2BoOXCf9PKAO31uAemx5wbnkcjfYXYsIZvWHaMF3%2BxNtPgDALp06gngWdEZxEdlzubnDWRTWNn5UQTWtk9c1aqfmu5LELd0QXrropWeTSpaqrQT8rO5zql5YB%2BxJlwQmIc4DzexNTInhHwSkqM60dukve9zkY4lKPXTol56ifNtAkdMCwm8RoaBnyC0QqdWb6zi77I00dl7w110q6rIJ9tvbQcxsQXqG9t0sR%2FXIOUQYAvB%2F0z3Ul%2BubLw8qnA428lH8EmkEsvX0KiBGccoq%2FaX3AxDpbNerTP%2BEQHr2tx5YTDnicnPBjqkAQkUAnqFSkIVAte9GmlpTBwudv35jVFzUzpEe2SXd2cJoqOqFbuG4IUFjYkFIct1%2BsA3N5O%2F8C55SATM97jx3SCOicbSUYZuqtOaNWYtxDMgFQmJ6OT45IfE4ytMlQKlhtysoZRv4gIssMOwR2UdkJd%2BoBjlXCzBiBCeXliIvxF5I0irIdxAxcB04UQGINiZ%2FSSSiUwu2QUjZkKwG1GIRDzR09J8&X-Amz-Signature=70817bb069bd5a91aecdd57e80347cfd78dfeb5daf5f3f7019fff12a88f0a6dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RM4KVHKH%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T191711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQD1Pkn6VLaj6QMXO8FCJZ4E4%2Fnhcd938YJVxuiv%2FjXRsAIhAIkehf6jp1eCiT0sVWdSbSORSgU%2Bh9r7Kzg4txCWqdBMKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzOlWtEPBrpASDSnhsq3AOEwFWaCZ%2FQgfUWtuT7xLo4Kem35amVCdaTejWXGZn5U1ywnWnrPjdCr5h7A%2BHnIvDbZDzXcXFP%2Bvv9Igymn5DezdF%2B3IbLDiT65cvjOFvr%2B2mHuL7YKEGUT%2FTgcFC29Cr8paRadoEgXYYcsdWZa9d5kN%2F8wlkh0DEH8yN%2FGYUeQV%2BzRn8vxIoX3mc1Sum99wRdQicH7poDGjRMu56vt9qEE4Ic6jA553JjPD6NytHqztO7jEJLRr4BJK5Q82v%2BReShzsssw63GSesxO6MIvshLDfQevmg%2F4yBMw5MdnREzlUyd0GYehYhs2iCk3t97YdswBlRtvVx5XHq40v%2BoOXCf9PKAO31uAemx5wbnkcjfYXYsIZvWHaMF3%2BxNtPgDALp06gngWdEZxEdlzubnDWRTWNn5UQTWtk9c1aqfmu5LELd0QXrropWeTSpaqrQT8rO5zql5YB%2BxJlwQmIc4DzexNTInhHwSkqM60dukve9zkY4lKPXTol56ifNtAkdMCwm8RoaBnyC0QqdWb6zi77I00dl7w110q6rIJ9tvbQcxsQXqG9t0sR%2FXIOUQYAvB%2F0z3Ul%2BubLw8qnA428lH8EmkEsvX0KiBGccoq%2FaX3AxDpbNerTP%2BEQHr2tx5YTDnicnPBjqkAQkUAnqFSkIVAte9GmlpTBwudv35jVFzUzpEe2SXd2cJoqOqFbuG4IUFjYkFIct1%2BsA3N5O%2F8C55SATM97jx3SCOicbSUYZuqtOaNWYtxDMgFQmJ6OT45IfE4ytMlQKlhtysoZRv4gIssMOwR2UdkJd%2BoBjlXCzBiBCeXliIvxF5I0irIdxAxcB04UQGINiZ%2FSSSiUwu2QUjZkKwG1GIRDzR09J8&X-Amz-Signature=3bfdd63123650182840c452b8300c793f21c4df8d593076d65fb9320320f25d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







