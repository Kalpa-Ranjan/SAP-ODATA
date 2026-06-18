



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWKZ4AHV%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T145624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA5cOg16IFilYcSuIq6lyOA7nkZ9fuE6X82PMP1Nk64%2BAiEA4OYpU7L0ctdaKCCjQuKTsieSDMmv0hIPlujzhN31dlUqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNLOO8xcCsdw0t%2BKxircA7NBQbXMotuQgRwhzoEs7fwscmaciPt5qNIDlQGm8I3b9gm%2Fyc0eRmOu%2FhcpPi8ELHEtdEchprW55zJ%2B%2BOdKp6I2qcJaEEMJSsHaMzAnKE1%2BDHWdDxiPwVvwRMcl%2FlB7jebkEYoKcUHATeYxo08rwA79BVPM3dOL5k1N42CMQ8uTOZiMxooIfZFa85TVxSgmLkwZZmtUV4Ugw3be9K87LP%2FAtLvBBFdXUOm0f0qXTiU7xmV%2Fe55sZvvV15Pd8I5PvLXQAUF2t450RmTY5GJ0YFzXHMtfjqxu%2BjPESEHcrOKVjn2waoeejKVv6h3y2aeBC%2Bi3O11aslf4NFNsAdBPFv8s2jb7iu5mIpT376CKLbWKhqxsZZ8tyKO1G8xFOt10O7G7rkg2WUHBJh1HY4M3FaIVRo7VAeLicvsrhnmDP31e9utw1HJyMKOIH5hSEmyFq3juPdTZ%2FyXn58Erv9G6Tj1AbsKh37TzfB9r9O5rAM2KXlT9Ceb%2F1RGDZ4gBRjd8kOABvu36U5Hl%2F5iiOq5%2Fxn8QfDMzK1XzBvvIhur%2FIGinM6hf6r0Apwono1ByLxScydN%2B6Hnfcqp1PQYuvLjwPzcg8eLzXU%2FerhMTfuuW6b8UahsA1DEhv02fweuvMMTnz9EGOqUBl7QUJlgeZpAbmybmOe4FhmLqvL%2BnWb%2FVLik%2FnrHe7BxfXuVNli1Sb4vaw0bGSu19tbd%2FWTzQKuCmtRKSh5lunaIvAkIfmenPEvycaBaawKiu4NiO04bNo7VRG7ju%2FbXI5CyHgedPtzp3FB%2FuMvYOlQSWRTkv6QFNIbq3jZ3RxQcqS2aLAKcIR5RfgONgxWwlTOQjn2wVIFs930tkztM9HcVPKz9m&X-Amz-Signature=68bb1320f36d66db5b65b4ad143ea7efb9af8e62f5d4eeee4d3096185ce101df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWKZ4AHV%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T145624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA5cOg16IFilYcSuIq6lyOA7nkZ9fuE6X82PMP1Nk64%2BAiEA4OYpU7L0ctdaKCCjQuKTsieSDMmv0hIPlujzhN31dlUqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNLOO8xcCsdw0t%2BKxircA7NBQbXMotuQgRwhzoEs7fwscmaciPt5qNIDlQGm8I3b9gm%2Fyc0eRmOu%2FhcpPi8ELHEtdEchprW55zJ%2B%2BOdKp6I2qcJaEEMJSsHaMzAnKE1%2BDHWdDxiPwVvwRMcl%2FlB7jebkEYoKcUHATeYxo08rwA79BVPM3dOL5k1N42CMQ8uTOZiMxooIfZFa85TVxSgmLkwZZmtUV4Ugw3be9K87LP%2FAtLvBBFdXUOm0f0qXTiU7xmV%2Fe55sZvvV15Pd8I5PvLXQAUF2t450RmTY5GJ0YFzXHMtfjqxu%2BjPESEHcrOKVjn2waoeejKVv6h3y2aeBC%2Bi3O11aslf4NFNsAdBPFv8s2jb7iu5mIpT376CKLbWKhqxsZZ8tyKO1G8xFOt10O7G7rkg2WUHBJh1HY4M3FaIVRo7VAeLicvsrhnmDP31e9utw1HJyMKOIH5hSEmyFq3juPdTZ%2FyXn58Erv9G6Tj1AbsKh37TzfB9r9O5rAM2KXlT9Ceb%2F1RGDZ4gBRjd8kOABvu36U5Hl%2F5iiOq5%2Fxn8QfDMzK1XzBvvIhur%2FIGinM6hf6r0Apwono1ByLxScydN%2B6Hnfcqp1PQYuvLjwPzcg8eLzXU%2FerhMTfuuW6b8UahsA1DEhv02fweuvMMTnz9EGOqUBl7QUJlgeZpAbmybmOe4FhmLqvL%2BnWb%2FVLik%2FnrHe7BxfXuVNli1Sb4vaw0bGSu19tbd%2FWTzQKuCmtRKSh5lunaIvAkIfmenPEvycaBaawKiu4NiO04bNo7VRG7ju%2FbXI5CyHgedPtzp3FB%2FuMvYOlQSWRTkv6QFNIbq3jZ3RxQcqS2aLAKcIR5RfgONgxWwlTOQjn2wVIFs930tkztM9HcVPKz9m&X-Amz-Signature=094d3c6fdf3088c8debcd4cbc29fc6763c39006d590c1bc6d2869556ea88eccf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







