



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N5RYWAT%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T023139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQDb35uO%2B2vIySHVvFHcb6UI9otvFZNqOvgH2WlsZoCVOgIhAJnRgkB%2BUBiidA8Sf2Yf5%2FIoZqHUTShoHyWzgJJyOSC8Kv8DCAMQABoMNjM3NDIzMTgzODA1IgyObFNbh972uxeIkIgq3AM6CopKmQRuUc%2B6MN%2B97rzfkCm%2FujVOwVCNx7C4F6IwPi9IiStwb4hcmxHyU%2FLYjEx5%2BEuLIvkG5HGYT3POFo4N39hF2CnS8VDYr5uY2jc7TUSvdCDDO6iiBB0O59R2ItSbxHUKfaBMFE4eom3xsooT7FIhy1oAcpPOhqrId5Y4g55wu9rztmcTy%2B8rpcQMTcS0dvDq05%2FR0FgXW585YcwLe%2FPu47IdPzMWni8%2F%2B5Ssq95UsuWjZTpkqGqM8DoLU89GC%2FT%2BoJ9vEuF%2F4%2BkBjhJFZpn9WweGnjgZTV0zwO6BTCvLSn3I4yrW%2FLey9DYUXitrgvgJu9t%2BAnnZj77KHURb%2BAYXm8tC%2FKTkpsc9C7mFmao90DDO%2BU48OfB0unHTcCF4I8%2BMH2yN6eg8TDGNp0%2B%2B8QxANebLlBaB3Vfw2XUMbJb74m2LjyIv3gISVDM%2F4ozKjaVe5EmUQss3IJT%2Fm2upcAVjh6PEGjyMwFghvo9vm7QDwsR0IwWimRtRSEkalnhj%2FRdmqZXM8OCjBIMFa2foei0fc0pXcLhOWgIByUNYRf2oGhlzyAgxGdjqDNqA4tFszsT51XmzMR9aX0cvFvw21FV8uxBUh79rB2EJrvJxlSeWxgcokotCB1ptkjCk58rPBjqkASeBNsreu6PbNdiZaU0UKVWPaVLB9GX2JUcOB64GdyPQuvkkJXgHKPo3JMLIfQCnWFprXgR4y3z5ngONdOdq4X7ffhsrun8h9Ww8ZL30swgcQW46nS3Yq9eoXmXd%2B7ceHfbMpfuaS4HWWaT8p3iGkGz7xHriQ2omn5%2Fh7nxZlPe6Q6DT3YiFO%2FcZlUMBOKXsCa5Y7ldH%2FOsclUEVaTGllVPBalh4&X-Amz-Signature=a06bade1c2ce6c93c8151ada6fa8771e680b2f28465d74fb6090a1f3932bccbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664N5RYWAT%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T023140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQDb35uO%2B2vIySHVvFHcb6UI9otvFZNqOvgH2WlsZoCVOgIhAJnRgkB%2BUBiidA8Sf2Yf5%2FIoZqHUTShoHyWzgJJyOSC8Kv8DCAMQABoMNjM3NDIzMTgzODA1IgyObFNbh972uxeIkIgq3AM6CopKmQRuUc%2B6MN%2B97rzfkCm%2FujVOwVCNx7C4F6IwPi9IiStwb4hcmxHyU%2FLYjEx5%2BEuLIvkG5HGYT3POFo4N39hF2CnS8VDYr5uY2jc7TUSvdCDDO6iiBB0O59R2ItSbxHUKfaBMFE4eom3xsooT7FIhy1oAcpPOhqrId5Y4g55wu9rztmcTy%2B8rpcQMTcS0dvDq05%2FR0FgXW585YcwLe%2FPu47IdPzMWni8%2F%2B5Ssq95UsuWjZTpkqGqM8DoLU89GC%2FT%2BoJ9vEuF%2F4%2BkBjhJFZpn9WweGnjgZTV0zwO6BTCvLSn3I4yrW%2FLey9DYUXitrgvgJu9t%2BAnnZj77KHURb%2BAYXm8tC%2FKTkpsc9C7mFmao90DDO%2BU48OfB0unHTcCF4I8%2BMH2yN6eg8TDGNp0%2B%2B8QxANebLlBaB3Vfw2XUMbJb74m2LjyIv3gISVDM%2F4ozKjaVe5EmUQss3IJT%2Fm2upcAVjh6PEGjyMwFghvo9vm7QDwsR0IwWimRtRSEkalnhj%2FRdmqZXM8OCjBIMFa2foei0fc0pXcLhOWgIByUNYRf2oGhlzyAgxGdjqDNqA4tFszsT51XmzMR9aX0cvFvw21FV8uxBUh79rB2EJrvJxlSeWxgcokotCB1ptkjCk58rPBjqkASeBNsreu6PbNdiZaU0UKVWPaVLB9GX2JUcOB64GdyPQuvkkJXgHKPo3JMLIfQCnWFprXgR4y3z5ngONdOdq4X7ffhsrun8h9Ww8ZL30swgcQW46nS3Yq9eoXmXd%2B7ceHfbMpfuaS4HWWaT8p3iGkGz7xHriQ2omn5%2Fh7nxZlPe6Q6DT3YiFO%2FcZlUMBOKXsCa5Y7ldH%2FOsclUEVaTGllVPBalh4&X-Amz-Signature=7a4a0cef5fcb7e839e97dff7fcb6fcb294b8bf45b16b04d808a95675e1627a5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







