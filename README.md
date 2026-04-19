



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYBIB6EX%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T184055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIG9VvJTGXq89yqhEnhsdCyZ7U5%2FOati0QUzs0knzkJOwAiEAyT88aClo%2B8la4t2p12EQcjwwD5r58c9pfMGJM7yghacq%2FwMICBAAGgw2Mzc0MjMxODM4MDUiDJHQh67hutoMi%2FjGtyrcA%2BvxDkSqllC8ovyPQ%2BgOC4UqP15jGx9YDAgFJb5tC%2BtB1uqg6Ivhx7%2BHy%2F6Cnm%2FasB3XqOC5t1RfooTE5XwWa5emn5FhzjVYymp7MZ4Nf4tZ1xMJm1AYDuRNhz6UPMT9TuyGpdA7%2FWvc5%2Bg%2FIf3NZXxNbsuizf%2FZQAxQtHjisIpdTV6710kbhaJq8h6RjuT36qOKwfXnEN1xpOcuMPjl9GBaqmN6ybGl2pWUzivAtf9Q9bTj2iMT0yoJadGudh4W3IeKtCEJidDQTTzVNK1bA6%2BgbBIMBpCMvUdI1wBVQ%2Fz%2FuGmx67kDZCRqN4UA8Vya0e6kdp4nTk%2BVfXT8WLkwFE6Powbg3D8M0OyOJULvgscJJn9NmFabh1SjMBLeLic00%2BVpdZQmGei%2BmnCEiAJ%2Bpp6c98npGHB8PKvySF6LCunRJOf2hgOXWDYIinlhhEWp6W49lCZ0iech%2FLH6%2F%2FO0bOBXjss8S22tqlQRCwKFtdgKzwXhUgbmohd5aXvdhpnorf6%2BLVXpyzun9GOZ0ixgJSF5eWLrUL0RRwHhepakTstOHOku%2B1PbJOZlzQHrduI7uInzcczISM32xPzPeOFLGF9bxIvxN8luxkwe0gBbLgy06JKSSMwG48vTry42MJjUk88GOqUBWvOw0OS68n6nCADtqL42WgoboZC5AU7xL2S0rl2WMo4CF%2BybuV%2BlF3TbApjii%2Bp%2B8PMPIGY0k8KNzN5f7n1bVk68IfBOXxFVzwFJpp6EsEmSdeSRe17QwmEFDTKZw5unybOf%2B5V1%2BLAFn5PZb%2BPaZS97dW4HtWr2ABJ1U0BpevZkwZ%2FWWYxEeq00teR6kivrrsidhieHM5JLerfXSWdd994Ki%2F5f&X-Amz-Signature=35eeb55bfb7aa458c883bf731bcca18390fa2dd89056413b8563c1774c8c5a42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYBIB6EX%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T184055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIG9VvJTGXq89yqhEnhsdCyZ7U5%2FOati0QUzs0knzkJOwAiEAyT88aClo%2B8la4t2p12EQcjwwD5r58c9pfMGJM7yghacq%2FwMICBAAGgw2Mzc0MjMxODM4MDUiDJHQh67hutoMi%2FjGtyrcA%2BvxDkSqllC8ovyPQ%2BgOC4UqP15jGx9YDAgFJb5tC%2BtB1uqg6Ivhx7%2BHy%2F6Cnm%2FasB3XqOC5t1RfooTE5XwWa5emn5FhzjVYymp7MZ4Nf4tZ1xMJm1AYDuRNhz6UPMT9TuyGpdA7%2FWvc5%2Bg%2FIf3NZXxNbsuizf%2FZQAxQtHjisIpdTV6710kbhaJq8h6RjuT36qOKwfXnEN1xpOcuMPjl9GBaqmN6ybGl2pWUzivAtf9Q9bTj2iMT0yoJadGudh4W3IeKtCEJidDQTTzVNK1bA6%2BgbBIMBpCMvUdI1wBVQ%2Fz%2FuGmx67kDZCRqN4UA8Vya0e6kdp4nTk%2BVfXT8WLkwFE6Powbg3D8M0OyOJULvgscJJn9NmFabh1SjMBLeLic00%2BVpdZQmGei%2BmnCEiAJ%2Bpp6c98npGHB8PKvySF6LCunRJOf2hgOXWDYIinlhhEWp6W49lCZ0iech%2FLH6%2F%2FO0bOBXjss8S22tqlQRCwKFtdgKzwXhUgbmohd5aXvdhpnorf6%2BLVXpyzun9GOZ0ixgJSF5eWLrUL0RRwHhepakTstOHOku%2B1PbJOZlzQHrduI7uInzcczISM32xPzPeOFLGF9bxIvxN8luxkwe0gBbLgy06JKSSMwG48vTry42MJjUk88GOqUBWvOw0OS68n6nCADtqL42WgoboZC5AU7xL2S0rl2WMo4CF%2BybuV%2BlF3TbApjii%2Bp%2B8PMPIGY0k8KNzN5f7n1bVk68IfBOXxFVzwFJpp6EsEmSdeSRe17QwmEFDTKZw5unybOf%2B5V1%2BLAFn5PZb%2BPaZS97dW4HtWr2ABJ1U0BpevZkwZ%2FWWYxEeq00teR6kivrrsidhieHM5JLerfXSWdd994Ki%2F5f&X-Amz-Signature=392bddcf57f91b6a6c3ad6f6e6c13bb755cbbf129d64f0e9aa4ad03f214981b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







