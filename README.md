



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W72UYJ2H%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T125313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAMsEoKe0h606pdyL%2BcnlPUJr%2BHJE8y9sM1691GHGQUMAiBG539K7rZ2OEaj7BWRpA0rUyZIqtLir%2FByFm0HGM6iOyr%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIM2VrLjGuPAZjJ7nkMKtwDUqAtV6QoLgYSBXoHYFSh%2F3F6Vh287k1KvgtXQ0bfP11nfEL9Jqnygiuh0KKd7VJc1%2F0AIN7S3L1p%2BL5JwepEsXDeNIxih1%2FxtQ9Qu4lZ7KTq5EX23%2FSIIfY%2FjkUDgoHiv8IO%2FCuY%2FgG7ECyaHAFRtIWEESrEqqUxGlEVo3bAzbmc3qtpwFMSkoiNDgZbCr%2FWplFnrMjQL%2BEBpw7k5feFsdKeEO5rwIJ64JpMqB3gtSPx8Ysmuw4QJWpghAufyYKSkltlwBh9Te5DEUtLhI46fBDyW0NARFKV3lmT8bCMkA%2B8uqlSj%2FCi%2F%2BdQA%2FQz0BJh8tJb0U1tuJXcyXgkcvD0OoHAWqDwUjOTtY2sPKUXh%2FZ2E9blP1Yt9Hj67vpX21mOmq2808fazFSH3hebBXlcqP7J60O8jDEcIZDkmyhD%2BPVuOfEiJcFE47od71xmlxODhQxcUk5TuyHIhIpXV77cAPPCMc9z6gdRRMYIUCZ3pggr%2BVyVP4uQbFOlNSxzanJA3lV9UVsGod1KvjctfXR%2Fb3e%2BGWnbpVbeh1GHyXY2%2FY%2BxEPmIyfBsiow1ZnT9wCxatjgHIfMQXAGQ35vj0598PTB6H2wh284w27iP3yDGRTFxTbfRVIcP92PSQpEwo7PRzAY6pgEuWlfxy65xi2mZLdDxBhn0l3JfiKUn19XfZVaw%2B6kKDVKVf4RjAw3AY2a3HToCzAMu9l7v%2F%2BiPTJtkWyH8Y42Nzy0VyjJlIm9AfpsbBU%2Ff1N8IOvqTaG7P1iltiYYTSgR5hrh9j2l1FC%2B2y%2F0t%2FJBt7poAU1%2F4uo2LHxON%2FXTaoLeqT9pHBuA5ZlVqFz4l3Iaw9LFr%2FWVdgSf1TqRCbf0TVRQ0U4hE&X-Amz-Signature=8e199186a9f00d4a6e58ed3790361c07dca6b7683fbf5f9326d7bfc749e9f55e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W72UYJ2H%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T125313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAMsEoKe0h606pdyL%2BcnlPUJr%2BHJE8y9sM1691GHGQUMAiBG539K7rZ2OEaj7BWRpA0rUyZIqtLir%2FByFm0HGM6iOyr%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIM2VrLjGuPAZjJ7nkMKtwDUqAtV6QoLgYSBXoHYFSh%2F3F6Vh287k1KvgtXQ0bfP11nfEL9Jqnygiuh0KKd7VJc1%2F0AIN7S3L1p%2BL5JwepEsXDeNIxih1%2FxtQ9Qu4lZ7KTq5EX23%2FSIIfY%2FjkUDgoHiv8IO%2FCuY%2FgG7ECyaHAFRtIWEESrEqqUxGlEVo3bAzbmc3qtpwFMSkoiNDgZbCr%2FWplFnrMjQL%2BEBpw7k5feFsdKeEO5rwIJ64JpMqB3gtSPx8Ysmuw4QJWpghAufyYKSkltlwBh9Te5DEUtLhI46fBDyW0NARFKV3lmT8bCMkA%2B8uqlSj%2FCi%2F%2BdQA%2FQz0BJh8tJb0U1tuJXcyXgkcvD0OoHAWqDwUjOTtY2sPKUXh%2FZ2E9blP1Yt9Hj67vpX21mOmq2808fazFSH3hebBXlcqP7J60O8jDEcIZDkmyhD%2BPVuOfEiJcFE47od71xmlxODhQxcUk5TuyHIhIpXV77cAPPCMc9z6gdRRMYIUCZ3pggr%2BVyVP4uQbFOlNSxzanJA3lV9UVsGod1KvjctfXR%2Fb3e%2BGWnbpVbeh1GHyXY2%2FY%2BxEPmIyfBsiow1ZnT9wCxatjgHIfMQXAGQ35vj0598PTB6H2wh284w27iP3yDGRTFxTbfRVIcP92PSQpEwo7PRzAY6pgEuWlfxy65xi2mZLdDxBhn0l3JfiKUn19XfZVaw%2B6kKDVKVf4RjAw3AY2a3HToCzAMu9l7v%2F%2BiPTJtkWyH8Y42Nzy0VyjJlIm9AfpsbBU%2Ff1N8IOvqTaG7P1iltiYYTSgR5hrh9j2l1FC%2B2y%2F0t%2FJBt7poAU1%2F4uo2LHxON%2FXTaoLeqT9pHBuA5ZlVqFz4l3Iaw9LFr%2FWVdgSf1TqRCbf0TVRQ0U4hE&X-Amz-Signature=08a8237b8aa23e9e594ef1812c1f652acef98ea8ced8d920809b56e769c7302d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







