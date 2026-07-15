



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7ZDZ3RT%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T132453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJGMEQCIAvJEl3y7JNOgqBfRPyhHqMp814cdNm2d%2F0G9qKHpvgxAiBBTmvGTFH1g8KwrICvb3RTyzGfu6%2FZeVlajjxGWhWKBSr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMtJHcOBpQA3huZ%2BDWKtwDxwRnQTSTB3%2Bxv4A3vCcitGUNM0ylBRj%2F4GoYTejmiWMFAcRy5pA%2FQWkNyRD46OSe%2Fiox131DLw7o6xVhCA5pG47Ds5ms62iQD32D%2BQswSFbiQX3V8k6p0Tp0km0AW9xQp0e5VMzDYB1uEBlBV9xs8MVGoeAQ9zZTron%2Bc87UUR4ZDFQfE%2B43btWc8A3O1vxL%2BdzD8wx5bDGHbId2IzJUicfO7SzKt6jfW%2BLsuN%2FkyOCLnzuOMvZcciuCcqxRghfLRyo5RPMIsKbKLfF9eQ06wxqBV%2B7maOChnR4DHEXFDM7gYv47ZJYI2dz93yIaf5ANfdQOTtJekpCIBO4EglJXWJKaEmNtMzcSY4U4O%2Fe4AO2qIuoqXjb617ZCTmLvIwUgWyH1XP9b2F2rL%2FYI1plqBICf79KunuXyvnkLSNagHs%2FPmzp%2FnbCejw8OkLSQlh2jQaApJxB8TdiSUi%2Ftgbbc6VcRVhLzoJuWC1QeUPgfCaGDzDWW8pMB0oJo7MwlN4Gw7ck%2FEp7NgGPmrZfSVDU%2BqiSJbCcUP3VJjwWMRasWAazqj%2FAmOxBT0NN1PGFsWn0y2jrBivPWGY6hdiLs1aD8vuaxF1zMvi%2F0YWysS4FWEv%2BgKPkYpnU87xy3eagwp%2Fbd0gY6pgENmDsbYpCILjynRuomUJXeURG3yJf1ikMkCrOGm3bdpGUWBtFhIG5H3We837f5HYR61USBiNj4YN7phdSSBozgzb%2Fnc35efprsjcEGSgYbVfAoUmcpi5JI7U3n63xgF2fihG4girusvN%2FzvfFuOfuiVCAsYYD2WRFT1mKdk6cAhA99W1ReHHTvOack%2B2t%2BzjMUX5iR6Yu3P%2FlHcS0xjyxsLmpn%2F%2Bs1&X-Amz-Signature=acbb6e936f5cbeb17f4cbc0fcebbbba6dddb50f6a5aebefb938c4d741122dd61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7ZDZ3RT%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T132453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJGMEQCIAvJEl3y7JNOgqBfRPyhHqMp814cdNm2d%2F0G9qKHpvgxAiBBTmvGTFH1g8KwrICvb3RTyzGfu6%2FZeVlajjxGWhWKBSr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMtJHcOBpQA3huZ%2BDWKtwDxwRnQTSTB3%2Bxv4A3vCcitGUNM0ylBRj%2F4GoYTejmiWMFAcRy5pA%2FQWkNyRD46OSe%2Fiox131DLw7o6xVhCA5pG47Ds5ms62iQD32D%2BQswSFbiQX3V8k6p0Tp0km0AW9xQp0e5VMzDYB1uEBlBV9xs8MVGoeAQ9zZTron%2Bc87UUR4ZDFQfE%2B43btWc8A3O1vxL%2BdzD8wx5bDGHbId2IzJUicfO7SzKt6jfW%2BLsuN%2FkyOCLnzuOMvZcciuCcqxRghfLRyo5RPMIsKbKLfF9eQ06wxqBV%2B7maOChnR4DHEXFDM7gYv47ZJYI2dz93yIaf5ANfdQOTtJekpCIBO4EglJXWJKaEmNtMzcSY4U4O%2Fe4AO2qIuoqXjb617ZCTmLvIwUgWyH1XP9b2F2rL%2FYI1plqBICf79KunuXyvnkLSNagHs%2FPmzp%2FnbCejw8OkLSQlh2jQaApJxB8TdiSUi%2Ftgbbc6VcRVhLzoJuWC1QeUPgfCaGDzDWW8pMB0oJo7MwlN4Gw7ck%2FEp7NgGPmrZfSVDU%2BqiSJbCcUP3VJjwWMRasWAazqj%2FAmOxBT0NN1PGFsWn0y2jrBivPWGY6hdiLs1aD8vuaxF1zMvi%2F0YWysS4FWEv%2BgKPkYpnU87xy3eagwp%2Fbd0gY6pgENmDsbYpCILjynRuomUJXeURG3yJf1ikMkCrOGm3bdpGUWBtFhIG5H3We837f5HYR61USBiNj4YN7phdSSBozgzb%2Fnc35efprsjcEGSgYbVfAoUmcpi5JI7U3n63xgF2fihG4girusvN%2FzvfFuOfuiVCAsYYD2WRFT1mKdk6cAhA99W1ReHHTvOack%2B2t%2BzjMUX5iR6Yu3P%2FlHcS0xjyxsLmpn%2F%2Bs1&X-Amz-Signature=f6b5ccd080b037f47863934ae4b6bd01d51146103749cbc01a54c901ac7f275d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







