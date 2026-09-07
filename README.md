



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7XAP46M%2F20260907%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260907T061650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJIMEYCIQCFhMvo3gY%2BOOo7sgY90u4oV9JwlmiloHg8KRL3dozviQIhAJPd8c1jpqfTT50wTxpoIPRLjtYSb11WTf3uUnBvF%2BRHKv8DCDYQABoMNjM3NDIzMTgzODA1Igy6RvGXNVmUb5HIRuIq3APYwrfy%2FFKKzHlOw0TSHRCQuLYrxrJx%2BhhmymXsA%2FuL0WG6zbEfRV%2BENc41y%2BOxUWpRm0A%2BFgAet9B1FVHSylYJdAT%2Ftj4HFnyfBuDchQRiIqk0XJO7G497MlFEtPT%2F%2BQtEkGAgqLhlLPw5vXG9Q4%2BQtElAOGi89lP%2FGx39P5c%2FFsllzyotpDfR2aChGeHjwmKGxJb6pzINlIp%2BMTmQ73AQvNM%2F6SBKbwO1pfXqZrQDfCV30VCH39us2SMhlirQ%2Ba5MCW%2Ft1cN6SOxt7nQ88xSIojf7dcyLLU4KCKZabiMnD%2FnftRFp6yKbhpemopOltHhLRy6YdImQCgWYQOoYOa0%2BcG1QA2pcQjuztZxZYyeQgBxvpv7vH%2BpCqTx2iS%2BvW6cC54p8zNGYg6%2FiA4QqdwUmIrO8hUEZi2swYOsD5T6tQbWCn2jkS%2B2lvlp6Oc5hHZ4lgoBChma4N9peJ5SWVsVWLNrSkF2bVBMVHeU5yVcObt1EfXcdEqMNnzJwTzSiHhXTZmpUpiCiu5wZQCZpTlVU0MfGbgD0gv6jUjH9uxnWA0dVL9KXdplKOhr0xytTSE4QA9D0VOpk437jcxKVife8FFD1HpmVOy8Aj61oA7vmhyfX38PkeDCNNxhdbzDv%2B%2FjUBjqkATFSHHmRjcC3mGdkc4fMzmQpovHumiI%2FLlGAmUpNDfk7ukTcZVXA2xR1YeAVcuPrUe%2F6VSgg2zfb7%2FMWejZZSwIbswLeUML1OOP9IzntDrl%2BBe9KMskVGT%2BRkv%2F1EDUfY6DvCgqLFTRazFjFmKq2btFfwzf9kgOXsRLv3NKVHmTpTb1GLmCNwcwNPhEiYRK%2Bb9v1UyJT3AHuHjY%2B63fZPTRG75VG&X-Amz-Signature=4fb8c8699f1c3031cfd705a550937f347b43990ee9ad2a4a34a30aa7b821d004&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T7XAP46M%2F20260907%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260907T061650Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJIMEYCIQCFhMvo3gY%2BOOo7sgY90u4oV9JwlmiloHg8KRL3dozviQIhAJPd8c1jpqfTT50wTxpoIPRLjtYSb11WTf3uUnBvF%2BRHKv8DCDYQABoMNjM3NDIzMTgzODA1Igy6RvGXNVmUb5HIRuIq3APYwrfy%2FFKKzHlOw0TSHRCQuLYrxrJx%2BhhmymXsA%2FuL0WG6zbEfRV%2BENc41y%2BOxUWpRm0A%2BFgAet9B1FVHSylYJdAT%2Ftj4HFnyfBuDchQRiIqk0XJO7G497MlFEtPT%2F%2BQtEkGAgqLhlLPw5vXG9Q4%2BQtElAOGi89lP%2FGx39P5c%2FFsllzyotpDfR2aChGeHjwmKGxJb6pzINlIp%2BMTmQ73AQvNM%2F6SBKbwO1pfXqZrQDfCV30VCH39us2SMhlirQ%2Ba5MCW%2Ft1cN6SOxt7nQ88xSIojf7dcyLLU4KCKZabiMnD%2FnftRFp6yKbhpemopOltHhLRy6YdImQCgWYQOoYOa0%2BcG1QA2pcQjuztZxZYyeQgBxvpv7vH%2BpCqTx2iS%2BvW6cC54p8zNGYg6%2FiA4QqdwUmIrO8hUEZi2swYOsD5T6tQbWCn2jkS%2B2lvlp6Oc5hHZ4lgoBChma4N9peJ5SWVsVWLNrSkF2bVBMVHeU5yVcObt1EfXcdEqMNnzJwTzSiHhXTZmpUpiCiu5wZQCZpTlVU0MfGbgD0gv6jUjH9uxnWA0dVL9KXdplKOhr0xytTSE4QA9D0VOpk437jcxKVife8FFD1HpmVOy8Aj61oA7vmhyfX38PkeDCNNxhdbzDv%2B%2FjUBjqkATFSHHmRjcC3mGdkc4fMzmQpovHumiI%2FLlGAmUpNDfk7ukTcZVXA2xR1YeAVcuPrUe%2F6VSgg2zfb7%2FMWejZZSwIbswLeUML1OOP9IzntDrl%2BBe9KMskVGT%2BRkv%2F1EDUfY6DvCgqLFTRazFjFmKq2btFfwzf9kgOXsRLv3NKVHmTpTb1GLmCNwcwNPhEiYRK%2Bb9v1UyJT3AHuHjY%2B63fZPTRG75VG&X-Amz-Signature=f3ee12b20c5b9c193691d192e4949d218993b3b4e3ce77c64752cccaccf08115&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







