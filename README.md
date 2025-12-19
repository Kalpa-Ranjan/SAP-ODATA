



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTEW3EQH%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T062529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIIrE0SPS2KbIf1PNNr%2FpkTwvdWqc6tz3leGfWuhG7wAiAMlYRqrQMyoA6cGD%2FDswle%2BYZlOkAJClSsku50uNNRcCqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMCXQaokVjxLVg4S7KtwDC9Wn2oGBBqQOTTGX26laN1wZU9CYcD88HTtWtzkVXBd41s5cC%2BhlIOOutp02xljHuGjIlhSqtkc6O4cCpH0H64zBHfUOi05uRnzL5bw1ZFiqxcE5lN5ObH17wMUjzKHEJIQ%2B1VIvP8zbi7AbQFQvjM%2BNZlJrtRvvssfPyxqm3VMA1oO8rPJw9KwOG2v0%2BgSoZD2YlwZC6u8aTinHrzqlVqi33BpZkviFQeOZ8AKVGGlDhQVNObSrqIHQTSylEczeXeT2%2BXt%2BotKqj2osldy4FLXPomJLhF0AVaaDf1VeNLHV3opuvxe31izTA8hAHQHBqApGVUiibVu%2Bz%2FRnWWMnQpjaaa%2BE%2FtCV6FS%2FQ5ix6gaEnLFebRJ4IHwaI8kFAxj5%2BtMZTg4WuN5Ui9%2FIiToJXHhB4hyGgASNWRBln%2FioLdsSNQKjekAER3dFuGRCUUACnvCdcKyBpHQvVm0oC3az97gpORReR%2Fw%2B04J6q5t6M6kQmJs4utr509KjSdyMZ3OKfz6qETCI1CW2ZxGAKTEqI5bWSQ9kCgBOKRmuukBGW2yeFgrIJKeyekoWMhNFdG26blxw2TJZicXo1tleMghuJN5fIdS9oks9qeP7AfEd2EB9Rcny2wGpUEyEVygwqcuTygY6pgF6DK3YRGFZDHs5vYSUKujQlH%2FtX1lS1O0IrfvEcw4P5o6mxfucIWFBTEuTE244Ps18FGyv%2B70Ut%2F%2Fhk78y%2Bbh6IcQ9FbaKqNxxxhmUBBTK70XMvZoiD1JnJ3WodZnXcSytIoxB3LXXjQMYw6k%2BJ%2Bnz5SHM2EoHZEdpTYptfhJKq69NJwJ2K0qBIVKB2CN%2FSjjd1ZoyQNo0LWjIwmUey%2FVzn7Iwa8d%2B&X-Amz-Signature=beaea5abc773df1775780b118e0e8ef074f31f63da2500c35b7024c6b1ca5184&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTEW3EQH%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T062529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIIrE0SPS2KbIf1PNNr%2FpkTwvdWqc6tz3leGfWuhG7wAiAMlYRqrQMyoA6cGD%2FDswle%2BYZlOkAJClSsku50uNNRcCqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMCXQaokVjxLVg4S7KtwDC9Wn2oGBBqQOTTGX26laN1wZU9CYcD88HTtWtzkVXBd41s5cC%2BhlIOOutp02xljHuGjIlhSqtkc6O4cCpH0H64zBHfUOi05uRnzL5bw1ZFiqxcE5lN5ObH17wMUjzKHEJIQ%2B1VIvP8zbi7AbQFQvjM%2BNZlJrtRvvssfPyxqm3VMA1oO8rPJw9KwOG2v0%2BgSoZD2YlwZC6u8aTinHrzqlVqi33BpZkviFQeOZ8AKVGGlDhQVNObSrqIHQTSylEczeXeT2%2BXt%2BotKqj2osldy4FLXPomJLhF0AVaaDf1VeNLHV3opuvxe31izTA8hAHQHBqApGVUiibVu%2Bz%2FRnWWMnQpjaaa%2BE%2FtCV6FS%2FQ5ix6gaEnLFebRJ4IHwaI8kFAxj5%2BtMZTg4WuN5Ui9%2FIiToJXHhB4hyGgASNWRBln%2FioLdsSNQKjekAER3dFuGRCUUACnvCdcKyBpHQvVm0oC3az97gpORReR%2Fw%2B04J6q5t6M6kQmJs4utr509KjSdyMZ3OKfz6qETCI1CW2ZxGAKTEqI5bWSQ9kCgBOKRmuukBGW2yeFgrIJKeyekoWMhNFdG26blxw2TJZicXo1tleMghuJN5fIdS9oks9qeP7AfEd2EB9Rcny2wGpUEyEVygwqcuTygY6pgF6DK3YRGFZDHs5vYSUKujQlH%2FtX1lS1O0IrfvEcw4P5o6mxfucIWFBTEuTE244Ps18FGyv%2B70Ut%2F%2Fhk78y%2Bbh6IcQ9FbaKqNxxxhmUBBTK70XMvZoiD1JnJ3WodZnXcSytIoxB3LXXjQMYw6k%2BJ%2Bnz5SHM2EoHZEdpTYptfhJKq69NJwJ2K0qBIVKB2CN%2FSjjd1ZoyQNo0LWjIwmUey%2FVzn7Iwa8d%2B&X-Amz-Signature=fbc1fe8986d86f7bb01d94f182031e57af56d5a3cfdc94d6ca9d2e8aa5211b9d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







