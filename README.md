



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SKGRGER%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T012113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQDcFozJnXgimUX6Jz0Xba8TLksKckuCFzjD9ZJXEQrCJAIgA5lTZ%2FqBHb%2F46ZHno5f967cUmDcafkfbictyLpzpCqgqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIGsNS4STUVfYFYdsSrcA6oPLCvz9SAbZ%2BYWcEA%2F7HnNgPHyuocg0TidBHmSCWsddwxXEzO%2FDhaBkdy4sZO00HdohG3nDIXjOP7DVfRnMOTSFqmoa95aZJS4jWHfSxNurgHciIxa87alS4%2BPDePgGYlG7zr3%2F%2BILp0knyxXsLS8S6ov6IQnOMFFob2IkBrjSu4libkss3nYAPHiH2WzmBaitOPqpJatiT80nL%2FMK%2FVDZt%2BK83F8sgJrVCw%2F7uDbe%2FpGAPC1Z1ieIxdS0%2FEyAhfkXa4y3vc6Q8L9ayH647MF1RdyyWv5YIpITPIf2Iww7JjjACh36SVXO2XmY3JL9KQOXghLpmOdU83f%2FQrcoev5FNunp9PERzfXs49VOzIqZsKvFED8mmNozkclSZy1AtnO5V0zfMz7uBArTHzbJC%2FdZFbXl8Yg2HvfwNPZQxncismIX52D04ZhxgVSKN7GMeFLELHRNiH8QG3inJW19FuldtZBVd1Wk4T0OiGSOekrfmn2Eq9SoKETgK2EzvOmatIColraGg1Um5eONQTWLSSEkfEUQnXX3P2vI9eLP9agGYNcpdFyiQMsQqZlslQCIExwA5Z9mBWgz2B2GxFfeiGbnk%2F%2Fyrm8dwVaeu%2B0Ijp%2FI4incE7A0xN1Vu%2FoxMLzhrckGOqUBVnH3MBEG%2BRAMjqc7DHk%2Bn%2BBn16i6VS%2BxYmdnQ9rY7umaeYtXXTwTa46cq%2FU8mHD02%2FO08F2QxM0t2WbTwxcA4vjYq6jO%2BfW46UNH3QRjFS0pYkXcj8Et%2BXpO4uEFAMvtv7yFbUeKdYQgci1KV%2BYpPttrdlZmwFncbeP0Ej5H7yr8F%2B%2BTNyD0tI2QIAmezJ%2FgFA9FTccsKzClIVYhF%2BfhLNXOGsXo&X-Amz-Signature=192e002379e39fb9cbbe63c61d7edf20fff085474c552bef29682efc4713979d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SKGRGER%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T012113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQDcFozJnXgimUX6Jz0Xba8TLksKckuCFzjD9ZJXEQrCJAIgA5lTZ%2FqBHb%2F46ZHno5f967cUmDcafkfbictyLpzpCqgqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIGsNS4STUVfYFYdsSrcA6oPLCvz9SAbZ%2BYWcEA%2F7HnNgPHyuocg0TidBHmSCWsddwxXEzO%2FDhaBkdy4sZO00HdohG3nDIXjOP7DVfRnMOTSFqmoa95aZJS4jWHfSxNurgHciIxa87alS4%2BPDePgGYlG7zr3%2F%2BILp0knyxXsLS8S6ov6IQnOMFFob2IkBrjSu4libkss3nYAPHiH2WzmBaitOPqpJatiT80nL%2FMK%2FVDZt%2BK83F8sgJrVCw%2F7uDbe%2FpGAPC1Z1ieIxdS0%2FEyAhfkXa4y3vc6Q8L9ayH647MF1RdyyWv5YIpITPIf2Iww7JjjACh36SVXO2XmY3JL9KQOXghLpmOdU83f%2FQrcoev5FNunp9PERzfXs49VOzIqZsKvFED8mmNozkclSZy1AtnO5V0zfMz7uBArTHzbJC%2FdZFbXl8Yg2HvfwNPZQxncismIX52D04ZhxgVSKN7GMeFLELHRNiH8QG3inJW19FuldtZBVd1Wk4T0OiGSOekrfmn2Eq9SoKETgK2EzvOmatIColraGg1Um5eONQTWLSSEkfEUQnXX3P2vI9eLP9agGYNcpdFyiQMsQqZlslQCIExwA5Z9mBWgz2B2GxFfeiGbnk%2F%2Fyrm8dwVaeu%2B0Ijp%2FI4incE7A0xN1Vu%2FoxMLzhrckGOqUBVnH3MBEG%2BRAMjqc7DHk%2Bn%2BBn16i6VS%2BxYmdnQ9rY7umaeYtXXTwTa46cq%2FU8mHD02%2FO08F2QxM0t2WbTwxcA4vjYq6jO%2BfW46UNH3QRjFS0pYkXcj8Et%2BXpO4uEFAMvtv7yFbUeKdYQgci1KV%2BYpPttrdlZmwFncbeP0Ej5H7yr8F%2B%2BTNyD0tI2QIAmezJ%2FgFA9FTccsKzClIVYhF%2BfhLNXOGsXo&X-Amz-Signature=ec782b12c051ada66c39c8e6a7df90d745bbfa1e1dabdd73f6c71fe6fccda3c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







