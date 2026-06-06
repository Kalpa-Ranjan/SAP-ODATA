



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WI5XGTFN%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T082735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC67XgrJMHVaWjjIrXN%2F%2Bf14kLw%2Fm%2B3Oe362vSDP3eWLAIhAOmd32wHLn8pT4eXB33GLr%2BLmMP6eIkriwWJu9rVy6bPKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydqfFeaAAISPDFy18q3AMK2xvfUQxrUBvOA04N076ksqgsi4BZVhf2RNki5EUVbdcd1N76uyxbcTqbmGJ72lu%2FA8kSZTRL%2F%2BAhYGco15rOuRcnBV6aFaHK32QXHfjeqNznC9NqHxDs2IYjXS9wZlYfK5IS6tf2Pug0XhPWpck0e3j5ua%2BgC2DqOA%2BE4Ssk4ntQeFP8rBlh4WcsVTIjyuIy1d6DJrc5Elaw6lriIH4Xhp%2FV1nGuhEXokIdXzY1lcVoWMV0Rwcnif78Z3qVeWP8WmZG0RHavWZn4cmYAejvDSxwzU8Tz1XWU%2FmLeVNNCXvSQdA%2BmxfM8W0j7naVYtrlcFSBjl9wqIRFI8e1eY7m8vjJGqLNiEX2zRyAOYmPlHqdLl8HiLRVsF5d9X5L%2B0k%2BGufawuZmiVyk9Ubx9OgYMIgUfDWq%2ByPNK3fcDV6Hs6yjYe08x2rjkW2bu%2FrTg6ATz0MRnRFVx2VKOS1dg%2FxBRxyb6jpbM2DEyYtsFFojg69ZlIcndLjJAe9ScSGWKGadStWEDs82oUNUBwaDyrRJbBiE3CtGagMtWlZXao51ejxq9OxHnVUgQAmVNETBy1bjAbUm9%2B3nrdrWbNrLAUixgJ6hXeSSkIedvI1WkOJ%2F1dPaq2jEvJ%2BXbPAXsljDWrI%2FRBjqkAfRaYTMcpJhmIgMZ9shRsiT4BhSKFVR3G7qAcF6hGhumXMpX1HS0WMt42Jjy3XLd9aV78ZVZcmnZOLwd%2FW3EjPyu9ngG690olM8BYF%2FF91di5kfUWYHyQrH38GpNH7D17a6wXkP%2FrQ8APuncX4lGswBoVqgxvu10UAQKj5%2BOEcNhb04tPDbUYr5idJFQAVk0mM6Ccu5VSkZYeS1zNu%2FtzOPOCQdN&X-Amz-Signature=8e0bd5f85b168246aa47aff278c0abd351d112336fab51baef92e4461b2d326d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WI5XGTFN%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T082735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC67XgrJMHVaWjjIrXN%2F%2Bf14kLw%2Fm%2B3Oe362vSDP3eWLAIhAOmd32wHLn8pT4eXB33GLr%2BLmMP6eIkriwWJu9rVy6bPKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgydqfFeaAAISPDFy18q3AMK2xvfUQxrUBvOA04N076ksqgsi4BZVhf2RNki5EUVbdcd1N76uyxbcTqbmGJ72lu%2FA8kSZTRL%2F%2BAhYGco15rOuRcnBV6aFaHK32QXHfjeqNznC9NqHxDs2IYjXS9wZlYfK5IS6tf2Pug0XhPWpck0e3j5ua%2BgC2DqOA%2BE4Ssk4ntQeFP8rBlh4WcsVTIjyuIy1d6DJrc5Elaw6lriIH4Xhp%2FV1nGuhEXokIdXzY1lcVoWMV0Rwcnif78Z3qVeWP8WmZG0RHavWZn4cmYAejvDSxwzU8Tz1XWU%2FmLeVNNCXvSQdA%2BmxfM8W0j7naVYtrlcFSBjl9wqIRFI8e1eY7m8vjJGqLNiEX2zRyAOYmPlHqdLl8HiLRVsF5d9X5L%2B0k%2BGufawuZmiVyk9Ubx9OgYMIgUfDWq%2ByPNK3fcDV6Hs6yjYe08x2rjkW2bu%2FrTg6ATz0MRnRFVx2VKOS1dg%2FxBRxyb6jpbM2DEyYtsFFojg69ZlIcndLjJAe9ScSGWKGadStWEDs82oUNUBwaDyrRJbBiE3CtGagMtWlZXao51ejxq9OxHnVUgQAmVNETBy1bjAbUm9%2B3nrdrWbNrLAUixgJ6hXeSSkIedvI1WkOJ%2F1dPaq2jEvJ%2BXbPAXsljDWrI%2FRBjqkAfRaYTMcpJhmIgMZ9shRsiT4BhSKFVR3G7qAcF6hGhumXMpX1HS0WMt42Jjy3XLd9aV78ZVZcmnZOLwd%2FW3EjPyu9ngG690olM8BYF%2FF91di5kfUWYHyQrH38GpNH7D17a6wXkP%2FrQ8APuncX4lGswBoVqgxvu10UAQKj5%2BOEcNhb04tPDbUYr5idJFQAVk0mM6Ccu5VSkZYeS1zNu%2FtzOPOCQdN&X-Amz-Signature=fe218f648e679df765b6e04e0e74756e6b1a2b242fc37b6a2e730996e78b8110&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







