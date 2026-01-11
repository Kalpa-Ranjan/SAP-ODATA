



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W5BVNUI%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T123202Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIAOOrHaX9Jc6vs1%2FprnVpTl5iDbywWZIJSRxoMwfsr3xAiEAnA99OvuSGQf7A9jNZ0zKuTsQXN9cn8QmlHgD8lFxo8cqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFJEjmFzlIFadD8LXSrcAyPIqw6X3humAAu12fkcqHSCry8RV%2FZw9TIYK33hHlP5tujQ9Bg2BZMnGtoMLn%2FP7F8Zu5EUh2kNibyd5WJWmXQmtyCd9aruCi4vnKWtwbxEaeEAF5FovCKO%2FCPkwoz0Z17wwpjiJIAKPw1YqTxIkptq%2F719rVb8sNnsdYsihH%2Bde7dMcHB%2Bc1lnre3AUNa2wjN6%2Fwo7On3mcyw9%2FNiEcQEPPNCoFpgpXGLfKsdCW0GYsop%2FwZtWlcmUKdnwtN11ck8SoWYHKsxCd5sw2r2ourl%2BEJPlEhm85ewESk%2Fb6F2ND7gNFirj54G8iDf%2FSW4L5D20iaFdFEmbNEzzvFlKbJ1q2X3o7m2uFPPZRNsyCf%2Flfd6I9ZACasJIhBwRuqReEVkybEq2YWTVVa4xW6BuV38hjfHxkZ89N65gLbd0Ye%2Bvu9AbVgkVLOqx3dZ36y8wJjhZJQuqox4e1QIjQ%2FMqNWBQyLhIMRvmdUqbJCE%2BHP2hYFYdgwicD2nCQgay2sIfOQ4AglZsyMmZByHWbh1a%2Bd9HG9Ch0sqohRWSLCJ4b9ZkD6v185Wh6vrkn4daM%2BbPQvThOH7bQxo%2BbodmAnArRKJBzwE5DvyNQTrBOMaVKcou%2FL0cxRTd90O50eBqMICNjcsGOqUBhcN2RVUPPevK2AayU4BGg1goVxaxjmhqshpHZ96SKrIKij0nXkRe8K2aaeM%2BrkyHd5FfhuxdC%2BDjFyznK5S5xZoMYTgtpXgdMwdjRX3ghMX9r1Kftdg6ePXziGgwenqy8PPLDVUo3RyDpuPTCJ%2FXkS63nHfBWvALslWGjupdVSCghj3TuZgz5492LFTiOupnBpKyGiSFIN2dpijEk3ZYtAfVrRyY&X-Amz-Signature=311e5906e2b3abd339daf1b46756ace6a5e6ded774576dc904631239a2700d2d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662W5BVNUI%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T123203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIAOOrHaX9Jc6vs1%2FprnVpTl5iDbywWZIJSRxoMwfsr3xAiEAnA99OvuSGQf7A9jNZ0zKuTsQXN9cn8QmlHgD8lFxo8cqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFJEjmFzlIFadD8LXSrcAyPIqw6X3humAAu12fkcqHSCry8RV%2FZw9TIYK33hHlP5tujQ9Bg2BZMnGtoMLn%2FP7F8Zu5EUh2kNibyd5WJWmXQmtyCd9aruCi4vnKWtwbxEaeEAF5FovCKO%2FCPkwoz0Z17wwpjiJIAKPw1YqTxIkptq%2F719rVb8sNnsdYsihH%2Bde7dMcHB%2Bc1lnre3AUNa2wjN6%2Fwo7On3mcyw9%2FNiEcQEPPNCoFpgpXGLfKsdCW0GYsop%2FwZtWlcmUKdnwtN11ck8SoWYHKsxCd5sw2r2ourl%2BEJPlEhm85ewESk%2Fb6F2ND7gNFirj54G8iDf%2FSW4L5D20iaFdFEmbNEzzvFlKbJ1q2X3o7m2uFPPZRNsyCf%2Flfd6I9ZACasJIhBwRuqReEVkybEq2YWTVVa4xW6BuV38hjfHxkZ89N65gLbd0Ye%2Bvu9AbVgkVLOqx3dZ36y8wJjhZJQuqox4e1QIjQ%2FMqNWBQyLhIMRvmdUqbJCE%2BHP2hYFYdgwicD2nCQgay2sIfOQ4AglZsyMmZByHWbh1a%2Bd9HG9Ch0sqohRWSLCJ4b9ZkD6v185Wh6vrkn4daM%2BbPQvThOH7bQxo%2BbodmAnArRKJBzwE5DvyNQTrBOMaVKcou%2FL0cxRTd90O50eBqMICNjcsGOqUBhcN2RVUPPevK2AayU4BGg1goVxaxjmhqshpHZ96SKrIKij0nXkRe8K2aaeM%2BrkyHd5FfhuxdC%2BDjFyznK5S5xZoMYTgtpXgdMwdjRX3ghMX9r1Kftdg6ePXziGgwenqy8PPLDVUo3RyDpuPTCJ%2FXkS63nHfBWvALslWGjupdVSCghj3TuZgz5492LFTiOupnBpKyGiSFIN2dpijEk3ZYtAfVrRyY&X-Amz-Signature=4e61e0e18b3230a3a55eff0e8a468dda65e306092d6891f5eba4386b5a6a4820&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







