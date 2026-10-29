



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644WBA7DI%2F20261029%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261029T120846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIBVMGqh0No7Q3mxKBhc9Cyje07N46ElKt83qdTrFwPsFAiAjuYm5a6wFu39CimOVr8awwoCn8%2FzIJX17Ed5j56%2FfqSr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIM8gEmsykGPeTozY9PKtwDb%2BXKljiKkBKkGnTMJWyWO%2BqaB3uTTp4dDQD6fRgbx4HPw9M7DuCv5DKkevIyda2fSzLjb53tzgJzsZuLBkxfBCxU6iwyNWRGaXGAjmWinPh3WRJ3pIHyI%2BH8YbWcsV4Z2%2B0BZVKdH3C3vNiK9WEwwoJIwQ7EdJUbRXeN0Ej3Eteeakq9zoM4s5gd0NcfqmIRyuKNQ2D87NM55VhcXbDvhfWktNAghmXr1dPn1fbXtfj3tU999NnKhq1vrVjG69lceNG53ZvCr6by0%2Fruwu%2FP%2Fq0bH4Qe%2BeBzED%2F%2F8%2F8Tt5Rt2%2B2DZYMkjB99gKH5ZYRDIUEfvtTaRErJLQaoTnsxLOdM%2BTKlSlhemXP%2F%2F6CvyUbYFUtA5Nt7IH7UvYlkJ%2FU5bQDDUgt5fdA55vwx4TVCWHQk9Rc7e8HAdEG00VJQOC%2BnotT9j%2Bom23a4OoMDkXeTa%2FgbX8Hd2WROLYkL7ffc36UniUtxLYUomHqXjqjfQAkAWad3ZVnF%2FaCoX4P%2FrFt%2BKnWRLCbkVDc5oOt4cXRYYAyeRDCsv7Gkh9Esd8Rm%2B7sQgeBu%2FQ8z4koLxvP9HidMJTm9jx857VXNzvjxKDaK2l2Y5VepQuZzKB77HLN0TeLqSNW3hheO2ColIZowy8KM1wY6pgHf9H9qP%2B8OvXw38WU2PM2bzGuW9bDOjTJf9U5NqFkDwZhD4%2Fit2gtVCyE%2BxlJeELIV53poB%2F9E3R6ybofhEu6HAoRAFytQ9x2xy%2BH%2Fs8YXbvfCUBU16eF0NbQJo5QDv9ED%2B6Hoa0sOOD1Tb6Appam7%2FUfKpkA1Fnxx3V%2FhsFgRWdl5nRFjm9gSgyBVe3dYzcEE6Bc7wwyQ4Fivhn1VKe4spjqT1hYT&X-Amz-Signature=7cbbccfd6af0910ef0da3b1898b8ab01b65920647512118707150b08ef534be0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644WBA7DI%2F20261029%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261029T120846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIBVMGqh0No7Q3mxKBhc9Cyje07N46ElKt83qdTrFwPsFAiAjuYm5a6wFu39CimOVr8awwoCn8%2FzIJX17Ed5j56%2FfqSr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIM8gEmsykGPeTozY9PKtwDb%2BXKljiKkBKkGnTMJWyWO%2BqaB3uTTp4dDQD6fRgbx4HPw9M7DuCv5DKkevIyda2fSzLjb53tzgJzsZuLBkxfBCxU6iwyNWRGaXGAjmWinPh3WRJ3pIHyI%2BH8YbWcsV4Z2%2B0BZVKdH3C3vNiK9WEwwoJIwQ7EdJUbRXeN0Ej3Eteeakq9zoM4s5gd0NcfqmIRyuKNQ2D87NM55VhcXbDvhfWktNAghmXr1dPn1fbXtfj3tU999NnKhq1vrVjG69lceNG53ZvCr6by0%2Fruwu%2FP%2Fq0bH4Qe%2BeBzED%2F%2F8%2F8Tt5Rt2%2B2DZYMkjB99gKH5ZYRDIUEfvtTaRErJLQaoTnsxLOdM%2BTKlSlhemXP%2F%2F6CvyUbYFUtA5Nt7IH7UvYlkJ%2FU5bQDDUgt5fdA55vwx4TVCWHQk9Rc7e8HAdEG00VJQOC%2BnotT9j%2Bom23a4OoMDkXeTa%2FgbX8Hd2WROLYkL7ffc36UniUtxLYUomHqXjqjfQAkAWad3ZVnF%2FaCoX4P%2FrFt%2BKnWRLCbkVDc5oOt4cXRYYAyeRDCsv7Gkh9Esd8Rm%2B7sQgeBu%2FQ8z4koLxvP9HidMJTm9jx857VXNzvjxKDaK2l2Y5VepQuZzKB77HLN0TeLqSNW3hheO2ColIZowy8KM1wY6pgHf9H9qP%2B8OvXw38WU2PM2bzGuW9bDOjTJf9U5NqFkDwZhD4%2Fit2gtVCyE%2BxlJeELIV53poB%2F9E3R6ybofhEu6HAoRAFytQ9x2xy%2BH%2Fs8YXbvfCUBU16eF0NbQJo5QDv9ED%2B6Hoa0sOOD1Tb6Appam7%2FUfKpkA1Fnxx3V%2FhsFgRWdl5nRFjm9gSgyBVe3dYzcEE6Bc7wwyQ4Fivhn1VKe4spjqT1hYT&X-Amz-Signature=bcb0180392ab69019ff2854a24a353e02fbef4a7917cd4b60353d7e4bbaf77fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







