



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466227ZI3DP%2F20261020%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261020T061246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIAYmCgzEIj79mhCe8jGpY0qWa9sTb%2FbwNpyBS3ZDtftPAiEAwziesEVJ7HJNkS0E9AGqZMciS2ZdFKzpJKsFWC%2B26E4q%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDK02PfxaOf01fABsgCrcA3R9gA%2FcMJ4Sj9ELwdJzMqBjCnL6tR2Ivdabv3pPCdjXtahiyWS6vbiWeTy0TTdoUkHMiGVhgpbjmthEfY4W5ryYM1etgBvgj170c3G9Ne6uE4ZgcSBMqdRU4Ibj4OrwQAv6AhB8q45Aq9mO4Grjrojt6O92NSFfAFMOBw%2B14VvDNQa8XadePhuVe6mvM00S%2FWooKWa%2BitBoi34CUYeu0KtpT0%2Fm%2Ff29nx8Gqd3eDMxTbKdhekWg%2F6nYKs%2B3z3zzvz8DqDVpyihK75lmGTuCjDVZVSY87KTprD2zliwm%2B7jRoZ6vJdkvSOcFMJXpD5VI%2BpFLqdV2berU5KvRN7%2BjiIa997yiDXXjqz%2BM8N8JjqS7xHklDwgUZKOB630xi8xeXLayRp3HUfONF8P%2FBHDX%2FuLsfLW1NseOVHsKFLzgt2SJwkZqpYXgnVOzEF1nIm%2BqW7cdEpX45XMeMVJ6TkGpXBJxtUSvKIYYkvr2xtM14HkOiCVZdIHpi8Jpjt9uICI%2FZ%2F7l88VZUAz8uGJNfxSLLhDq8kbhPIfqbOZPEOTXYU0lmdrWKxl3tQbZ5kFjRskm9aTs2vdxe6o%2FM%2B%2F6wiZrAL9lTyJSuOr3YwpAgah0VoAUsNMjKKAQkfY1faHpMOLb29YGOqUBuvuuOnA0Jpsz8BR5%2F7yvJuhWmXiw9EJN%2BydLDN7oueSMxpSOZ8Q055dnldl9nh%2BFxGq6MRxxuFc0AreRhUv2cz0ccGkzPyrkKoCPhx%2FP%2FulxN3tQQT6hE%2BQE%2BI3maH2YLVcBV72NI5Jk%2FUvYGQe75c2meeTGJbUqv6L0ahjmD53ObPUEbvpCJoZUA%2F5WguUgCpIA42Q7xsiNYIlCgqXUafVw5%2FfL&X-Amz-Signature=7bb9fcd6304fea4d6fecb44ff2286ee58c086a5f343714ef6ac39c7d2913d40c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466227ZI3DP%2F20261020%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261020T061246Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIAYmCgzEIj79mhCe8jGpY0qWa9sTb%2FbwNpyBS3ZDtftPAiEAwziesEVJ7HJNkS0E9AGqZMciS2ZdFKzpJKsFWC%2B26E4q%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDK02PfxaOf01fABsgCrcA3R9gA%2FcMJ4Sj9ELwdJzMqBjCnL6tR2Ivdabv3pPCdjXtahiyWS6vbiWeTy0TTdoUkHMiGVhgpbjmthEfY4W5ryYM1etgBvgj170c3G9Ne6uE4ZgcSBMqdRU4Ibj4OrwQAv6AhB8q45Aq9mO4Grjrojt6O92NSFfAFMOBw%2B14VvDNQa8XadePhuVe6mvM00S%2FWooKWa%2BitBoi34CUYeu0KtpT0%2Fm%2Ff29nx8Gqd3eDMxTbKdhekWg%2F6nYKs%2B3z3zzvz8DqDVpyihK75lmGTuCjDVZVSY87KTprD2zliwm%2B7jRoZ6vJdkvSOcFMJXpD5VI%2BpFLqdV2berU5KvRN7%2BjiIa997yiDXXjqz%2BM8N8JjqS7xHklDwgUZKOB630xi8xeXLayRp3HUfONF8P%2FBHDX%2FuLsfLW1NseOVHsKFLzgt2SJwkZqpYXgnVOzEF1nIm%2BqW7cdEpX45XMeMVJ6TkGpXBJxtUSvKIYYkvr2xtM14HkOiCVZdIHpi8Jpjt9uICI%2FZ%2F7l88VZUAz8uGJNfxSLLhDq8kbhPIfqbOZPEOTXYU0lmdrWKxl3tQbZ5kFjRskm9aTs2vdxe6o%2FM%2B%2F6wiZrAL9lTyJSuOr3YwpAgah0VoAUsNMjKKAQkfY1faHpMOLb29YGOqUBuvuuOnA0Jpsz8BR5%2F7yvJuhWmXiw9EJN%2BydLDN7oueSMxpSOZ8Q055dnldl9nh%2BFxGq6MRxxuFc0AreRhUv2cz0ccGkzPyrkKoCPhx%2FP%2FulxN3tQQT6hE%2BQE%2BI3maH2YLVcBV72NI5Jk%2FUvYGQe75c2meeTGJbUqv6L0ahjmD53ObPUEbvpCJoZUA%2F5WguUgCpIA42Q7xsiNYIlCgqXUafVw5%2FfL&X-Amz-Signature=72d22adcac4fda22163ef366d0e58ecc6a5da6e60a74831df3c0ec5fa5d3d8a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







