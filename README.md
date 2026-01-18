



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPUJC5A4%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T123109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFwtSuGfoFHJOS94yfZLH873N6e9sO7TzBKCVqQXt1%2BwAiEAucBRNcY3XK%2Ftsi8L9td0jomZCwc9Y%2FddS7jiwwp2Uacq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDNQbtIfO1kiUx1SBYSrcA9IXq3M2jLVmAw2XHbKZTfiHXIsMFkFmtda60v77KLdoq%2BmmUyJgJYmhU1Zd3PKXZhzNkXOuHal5Q9rSPKnSX%2BCVqL1wDGKvZKpgCxfwhP0GsAXNMqQ72DMHVO4XDEUshcXANKD6xQzIYCSyjZjk%2F4Rif582Db9PwVD3GXlKn9AtGeFvFifsl15UXQLQBInWDwJ57E13pUKq%2FO8IhsQ9cLoAtXgfVfp4IlFZ5ELYqC6%2BsccXcFND700SBpnfw44vy0huwa5IDhK1r5f%2FCUrcysDWuVZb7FiuWcIeqV5u70%2BFAI4iZu29adhvM2mbBfl%2Blrxk3cV%2BCy2VIeDUUhoDtWt95zntRezuxTbzxrFjKcMVeiR8nPmKD4%2BpaDCdPHwIbvlX1egPSUxV12XyTKMrxbEow%2BbPRc3rKIVmvNmPL3c9rpJ4ZSxdLgKMDo%2F2k%2B7QO1w3U1HU%2BRAr71ReNdu9AZGaAL%2Bj35Bom8BKa9MiZpMQAtBgU%2FlcoZv0fht4TsfY5mJLeHOgVm5iNyk%2FqJt20IaCQOT4PJHTYAbxFcG54d24FHOcl5tJxui9Gu0KODla6WjAYT8GLyPaCCc7F7Hhn1Zww5VpU0%2FlLlc0HUcujOW7KejfsJUekNMsLgK1MMnGsssGOqUBbTqIsviaKXznU9fBDWmd6OkvPkV4UmrKvfrXHyX8ZnaaEldeUYexrXjc44al7Mj7URHDsZZqARP4hzsi3TovzPIpm9c%2BuiUUQ4pxTz2KfyJg832fs7JkwPrlEXfdO2hwUWfwYCn9YSFAwYI%2BOW5BhxBabbTGuL5bRdq3HOwnLt7e9zKNAKeoIKEhYB9IXMCX%2BiTU%2BZAA7b017jMVqdJlrOIeRwaS&X-Amz-Signature=d9aac32df7ccfeb737e4f20e447f955dd8c046420070fbb581dc1d7c78860d70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPUJC5A4%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T123109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFwtSuGfoFHJOS94yfZLH873N6e9sO7TzBKCVqQXt1%2BwAiEAucBRNcY3XK%2Ftsi8L9td0jomZCwc9Y%2FddS7jiwwp2Uacq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDNQbtIfO1kiUx1SBYSrcA9IXq3M2jLVmAw2XHbKZTfiHXIsMFkFmtda60v77KLdoq%2BmmUyJgJYmhU1Zd3PKXZhzNkXOuHal5Q9rSPKnSX%2BCVqL1wDGKvZKpgCxfwhP0GsAXNMqQ72DMHVO4XDEUshcXANKD6xQzIYCSyjZjk%2F4Rif582Db9PwVD3GXlKn9AtGeFvFifsl15UXQLQBInWDwJ57E13pUKq%2FO8IhsQ9cLoAtXgfVfp4IlFZ5ELYqC6%2BsccXcFND700SBpnfw44vy0huwa5IDhK1r5f%2FCUrcysDWuVZb7FiuWcIeqV5u70%2BFAI4iZu29adhvM2mbBfl%2Blrxk3cV%2BCy2VIeDUUhoDtWt95zntRezuxTbzxrFjKcMVeiR8nPmKD4%2BpaDCdPHwIbvlX1egPSUxV12XyTKMrxbEow%2BbPRc3rKIVmvNmPL3c9rpJ4ZSxdLgKMDo%2F2k%2B7QO1w3U1HU%2BRAr71ReNdu9AZGaAL%2Bj35Bom8BKa9MiZpMQAtBgU%2FlcoZv0fht4TsfY5mJLeHOgVm5iNyk%2FqJt20IaCQOT4PJHTYAbxFcG54d24FHOcl5tJxui9Gu0KODla6WjAYT8GLyPaCCc7F7Hhn1Zww5VpU0%2FlLlc0HUcujOW7KejfsJUekNMsLgK1MMnGsssGOqUBbTqIsviaKXznU9fBDWmd6OkvPkV4UmrKvfrXHyX8ZnaaEldeUYexrXjc44al7Mj7URHDsZZqARP4hzsi3TovzPIpm9c%2BuiUUQ4pxTz2KfyJg832fs7JkwPrlEXfdO2hwUWfwYCn9YSFAwYI%2BOW5BhxBabbTGuL5bRdq3HOwnLt7e9zKNAKeoIKEhYB9IXMCX%2BiTU%2BZAA7b017jMVqdJlrOIeRwaS&X-Amz-Signature=af38d569b431a3520313fd796ee1ea6716df76bf2d3548a3674946acb55fff86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







