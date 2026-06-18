



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5QHIMY5%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T101319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPqbOraGNyyxwbdxNdDtCX2uUH6z1gwe1YSVDumK4d%2FAIhAPUyLBtmGecO9Ro4ReqHZGIgbOX61lfppnAdZ2193LJ8KogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZHRS089h4SeWtIogq3AP%2B%2FwBumxIIPPY4JbiezlNlbbE3IreNPLUWNX3boMqap1aArE%2FA2%2F%2BZDfhbT2mVqHZRsuAhOsGndLpWvUNv6JpkJ8I8KvcMqzxb2ufM1baLZEaWpEQ8yr6nJIz5v9QGd1s9yWbJsJUSjStXb8KOGIv20SjSCiOJ1MnNzIwgPBkTKO1bnsBDEYCgdC38IdrRHy1MSlYYEpRskIVTKwf%2F%2FYwcwdHrL99bzO0ZCYBFlqgXZb4T2tv08sMKb4HphWOqdJ0PdntSAc2I1MhViYPWeR4lKkoAUdbPexepu8RnGX%2FGF0RVIUNey8JGjBKcT8958h6k%2FVY3rxOUQkXd33kThc2jbh7d2NutYXH9GfmlmLaW4OZnuGE%2BEcpIPruhEODuf24PbwIHPjVtPZ0r%2BGZ4LndRaCHtJayh0OcNC7nSASHFzDrEGCs0vGrFIREtdF0dTk1XJg0wtLTvCxFsyOTKrHp79qIp01ZhRL%2F9KyWxkjy8v1%2Fs49cQaQs3OBY7meuEqdnSi10KdFGtquni5Y5%2BAA3alIW7GavcjHTUZb7p0vwNpBqfOomwtOc%2FwMCHKqxLsHV78TOqYJZjG5P49jv0H2DgIKjIIUGPi8oOePKgkWZA2KOHBuHIy9Ee9MLNsDD%2Fgs%2FRBjqkARF3DHu433CfUeC0kNSdcrBoZbQWiu0SrzmyyJn7GlMF2FQRUYEDvM9HMJv6rgzd6sO5VfuCm4RNyOV6aI4qIZJEZ%2BvQCC%2F%2B2Bzq2uyC71vRT3RYqhjauNaMjQdKkFTIVK%2BVIDbVH5y6JoSxvGtfA5uyp0gib8sLDGVub44oKq2acwpP7gd8FZRzqycBA7qJjkqsoPKSDdbvVsE7l5BnbVVNkm%2Bn&X-Amz-Signature=09b2ed659f0149aa0fa13c8b71c66cc86f90c86b646d0bba4f06c4f1ea2d0426&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5QHIMY5%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T101320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPqbOraGNyyxwbdxNdDtCX2uUH6z1gwe1YSVDumK4d%2FAIhAPUyLBtmGecO9Ro4ReqHZGIgbOX61lfppnAdZ2193LJ8KogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxZHRS089h4SeWtIogq3AP%2B%2FwBumxIIPPY4JbiezlNlbbE3IreNPLUWNX3boMqap1aArE%2FA2%2F%2BZDfhbT2mVqHZRsuAhOsGndLpWvUNv6JpkJ8I8KvcMqzxb2ufM1baLZEaWpEQ8yr6nJIz5v9QGd1s9yWbJsJUSjStXb8KOGIv20SjSCiOJ1MnNzIwgPBkTKO1bnsBDEYCgdC38IdrRHy1MSlYYEpRskIVTKwf%2F%2FYwcwdHrL99bzO0ZCYBFlqgXZb4T2tv08sMKb4HphWOqdJ0PdntSAc2I1MhViYPWeR4lKkoAUdbPexepu8RnGX%2FGF0RVIUNey8JGjBKcT8958h6k%2FVY3rxOUQkXd33kThc2jbh7d2NutYXH9GfmlmLaW4OZnuGE%2BEcpIPruhEODuf24PbwIHPjVtPZ0r%2BGZ4LndRaCHtJayh0OcNC7nSASHFzDrEGCs0vGrFIREtdF0dTk1XJg0wtLTvCxFsyOTKrHp79qIp01ZhRL%2F9KyWxkjy8v1%2Fs49cQaQs3OBY7meuEqdnSi10KdFGtquni5Y5%2BAA3alIW7GavcjHTUZb7p0vwNpBqfOomwtOc%2FwMCHKqxLsHV78TOqYJZjG5P49jv0H2DgIKjIIUGPi8oOePKgkWZA2KOHBuHIy9Ee9MLNsDD%2Fgs%2FRBjqkARF3DHu433CfUeC0kNSdcrBoZbQWiu0SrzmyyJn7GlMF2FQRUYEDvM9HMJv6rgzd6sO5VfuCm4RNyOV6aI4qIZJEZ%2BvQCC%2F%2B2Bzq2uyC71vRT3RYqhjauNaMjQdKkFTIVK%2BVIDbVH5y6JoSxvGtfA5uyp0gib8sLDGVub44oKq2acwpP7gd8FZRzqycBA7qJjkqsoPKSDdbvVsE7l5BnbVVNkm%2Bn&X-Amz-Signature=27afb2338e880abe96ae0196788a0c5f0090b089ef0bfafc5120ecf2d15f7f8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







