



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664U6VOCAQ%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T011537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDk8%2F5CCrjEzxwbROy79u1lUMwsU7fybfvPOchEgpO6ZAIgDi0hV7c6lT5%2BqjY9t9Ip6kB6ugHWjxopbW4uYt16rg4qiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNuc%2B2so9akuDog0xircA9PFgq0b2dr55Yj7Yk1L%2FQb36dVGZDaRYcMf8CxD%2FKDDe6%2FHsTGQk9VnDro1FzGXO78I5TsZjrH1KvZGAKHmDOdpgCf5pAA8%2BVEvuUyruAs9Ny0w6Zp4uQMMyBu%2FdSWvBC%2FqZgMH6gjaS3PoWbOY%2Buj%2FKBDS3IpG2kc%2F2PeSYV9T0edodiwhC6zPijnPfWt149oDmOjnZDUBPZjRnDw4FgFaah7n%2BnlsSTCiMOTp0eCLT8XBf0TMLKhOul6x8m02G6v9pu3nnXOssskjieX0j9E0PNuAAtzhQO6T3LCKA0TjTqSvmmxZLPAU25NK4RiBRf7xAZmKtuu54KuN7MLwa%2B1vK%2Fw8j02eaqfJjynD4vVqONu21DD3WRUiekO23z1xM7VpMQMJNPj5mn5t3svzyZ9QPwi7K4i7wCsWck4gdxtgQTdt6lA5Rvz0C%2F%2FxzYh27Il%2BGPXhc6P%2FEBeeFXQcYR1VihHGLwAwteg%2Fmt5R%2FObEvrcYuUFh2fU%2F1tTbu0ugvj56bG1JqaubAMWKsWmUokunfYcxVJKXvO2WrYu9GYb%2FzW6lY0FsGyJf9zVUdydjwIP1QNXuZU9Jxe85RJ8CUvxKxJSsxV8Egj%2FuUthD3cdQg99iCGFjsU6f5KAfMNOplssGOqUBI44NaPqBYRzwGM2Ecmkhd3F13LHv20IB4oTRU54s%2BDP80n8XmmBaPIdSTaY0kFCDWAbrN7BD8vrufoAxhAU1MVR6grpqom3XLrp6mHAqDxITzgLUi7FiVqA3Wb4OPRzzDAXVJhgVmdc%2BfJKAy5vatO5VwcxT%2FI%2FeZX%2BoEvtPEmFb2wiXuewdqdPia18z2NU%2Buqv7eF3c85kGpUbw%2FD%2BmXS9js%2BRj&X-Amz-Signature=abb3d32c4a8eba0b1bc67439df144b4a0c3afd45a4496e673bbe80e3705c4c6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664U6VOCAQ%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T011538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDk8%2F5CCrjEzxwbROy79u1lUMwsU7fybfvPOchEgpO6ZAIgDi0hV7c6lT5%2BqjY9t9Ip6kB6ugHWjxopbW4uYt16rg4qiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNuc%2B2so9akuDog0xircA9PFgq0b2dr55Yj7Yk1L%2FQb36dVGZDaRYcMf8CxD%2FKDDe6%2FHsTGQk9VnDro1FzGXO78I5TsZjrH1KvZGAKHmDOdpgCf5pAA8%2BVEvuUyruAs9Ny0w6Zp4uQMMyBu%2FdSWvBC%2FqZgMH6gjaS3PoWbOY%2Buj%2FKBDS3IpG2kc%2F2PeSYV9T0edodiwhC6zPijnPfWt149oDmOjnZDUBPZjRnDw4FgFaah7n%2BnlsSTCiMOTp0eCLT8XBf0TMLKhOul6x8m02G6v9pu3nnXOssskjieX0j9E0PNuAAtzhQO6T3LCKA0TjTqSvmmxZLPAU25NK4RiBRf7xAZmKtuu54KuN7MLwa%2B1vK%2Fw8j02eaqfJjynD4vVqONu21DD3WRUiekO23z1xM7VpMQMJNPj5mn5t3svzyZ9QPwi7K4i7wCsWck4gdxtgQTdt6lA5Rvz0C%2F%2FxzYh27Il%2BGPXhc6P%2FEBeeFXQcYR1VihHGLwAwteg%2Fmt5R%2FObEvrcYuUFh2fU%2F1tTbu0ugvj56bG1JqaubAMWKsWmUokunfYcxVJKXvO2WrYu9GYb%2FzW6lY0FsGyJf9zVUdydjwIP1QNXuZU9Jxe85RJ8CUvxKxJSsxV8Egj%2FuUthD3cdQg99iCGFjsU6f5KAfMNOplssGOqUBI44NaPqBYRzwGM2Ecmkhd3F13LHv20IB4oTRU54s%2BDP80n8XmmBaPIdSTaY0kFCDWAbrN7BD8vrufoAxhAU1MVR6grpqom3XLrp6mHAqDxITzgLUi7FiVqA3Wb4OPRzzDAXVJhgVmdc%2BfJKAy5vatO5VwcxT%2FI%2FeZX%2BoEvtPEmFb2wiXuewdqdPia18z2NU%2Buqv7eF3c85kGpUbw%2FD%2BmXS9js%2BRj&X-Amz-Signature=9a43d4576b595f450cc41398ffc0ad124fa10aadcf28d935517e2d3089e72fa9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







