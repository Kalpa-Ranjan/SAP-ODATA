



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XVJ5ZR6%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T181925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIEETSp3PoZ5HdOjhz6m3HBBDsD52k%2BW5ygc3kdVX9GQNAiByd4Uqvj5hfgWURAMFHhjfrCj3xQg1%2FlEd6BC%2F3A7mbCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMn7Ul6T6Elzng%2B94AKtwDzjzMwT0%2BzfdmtDQSoV0BtaRWLPV51psfL%2B301bxluekknQ%2FIVswcpo0IC4%2FRmZqrPcY8SODSoVP8kRw2mdFVo5cTxTLoXaocGI8w0PCfznvIi%2BHbZ%2BdZdKiB7qEoRDyeFLmjZ87hurHoQqmuQKSjSZ7%2BaGV8%2B3fYylbJ3L7r%2B7O9lpd4FkBdySjUtkocLDmr%2FafM%2FrtOOKY75OXWB%2BJTXjoautRk1cIQhqtK3JjVZ7JDgLBuVgbdVTNNXXjm53H6wIRpgLbsUOq85fLTDRaMe8enUS0ccHX7%2By%2F7B23uMVasEqxtjQ2wjV6VKR6L7DlSVI%2BScm6kuU91Lr46WG9OsybQGYzvdlN%2BhM2V4d%2FCkeo4f2j%2FryCsoF9hcC6vfQqbbmBoSSYGS35CUs1rydek0jofSUkzsbFRmfFNG4%2BrY2L0zA8B64XlUCSpmyM8U3tJglBNT2a4%2FIOWd%2FlKntTkVuBfKhTrzlUZdeD0JMMF2QbBfyGbfMgmW7MbIrUHBmJOP2fk2tr2dEO21PzvM6XY9Iu5Vh7L2zxSup2rrQmQ9ixHOPdEn%2F%2FwqKaZZREjgfPNP%2B2dx2T8uZonD9Lit9Cn%2Bq1cgvPQ0Z2Z9fXlmpYVwjhIsE5b583fTtD6Bkkw75XDyAY6pgHL2jGKn5SbzK8SDQaHz2cjv4WAzP7J2h9VEpvS76woTeh1dt7HgFu38gVmcCBAWrGosFuvi7DqOGGqukfso23HHoeTA1%2BGn97UsoH3hVGbfp0%2FIlxsf2ZdNmZ55q8yF70GS88vrXHgoQ%2FR97rMgU7gzO23RR6oskWl5HFjCuJt3bHC8662qIbsBGqZDII1aKmOykwVjKd3juUDx2%2Fwfu%2BYNKU8kuUJ&X-Amz-Signature=69f76a5569c35cdda59cb30bee1a003547e1d74bf27d67e18016854422a79ca6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XVJ5ZR6%2F20251109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251109T181925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIEETSp3PoZ5HdOjhz6m3HBBDsD52k%2BW5ygc3kdVX9GQNAiByd4Uqvj5hfgWURAMFHhjfrCj3xQg1%2FlEd6BC%2F3A7mbCqIBAjy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMn7Ul6T6Elzng%2B94AKtwDzjzMwT0%2BzfdmtDQSoV0BtaRWLPV51psfL%2B301bxluekknQ%2FIVswcpo0IC4%2FRmZqrPcY8SODSoVP8kRw2mdFVo5cTxTLoXaocGI8w0PCfznvIi%2BHbZ%2BdZdKiB7qEoRDyeFLmjZ87hurHoQqmuQKSjSZ7%2BaGV8%2B3fYylbJ3L7r%2B7O9lpd4FkBdySjUtkocLDmr%2FafM%2FrtOOKY75OXWB%2BJTXjoautRk1cIQhqtK3JjVZ7JDgLBuVgbdVTNNXXjm53H6wIRpgLbsUOq85fLTDRaMe8enUS0ccHX7%2By%2F7B23uMVasEqxtjQ2wjV6VKR6L7DlSVI%2BScm6kuU91Lr46WG9OsybQGYzvdlN%2BhM2V4d%2FCkeo4f2j%2FryCsoF9hcC6vfQqbbmBoSSYGS35CUs1rydek0jofSUkzsbFRmfFNG4%2BrY2L0zA8B64XlUCSpmyM8U3tJglBNT2a4%2FIOWd%2FlKntTkVuBfKhTrzlUZdeD0JMMF2QbBfyGbfMgmW7MbIrUHBmJOP2fk2tr2dEO21PzvM6XY9Iu5Vh7L2zxSup2rrQmQ9ixHOPdEn%2F%2FwqKaZZREjgfPNP%2B2dx2T8uZonD9Lit9Cn%2Bq1cgvPQ0Z2Z9fXlmpYVwjhIsE5b583fTtD6Bkkw75XDyAY6pgHL2jGKn5SbzK8SDQaHz2cjv4WAzP7J2h9VEpvS76woTeh1dt7HgFu38gVmcCBAWrGosFuvi7DqOGGqukfso23HHoeTA1%2BGn97UsoH3hVGbfp0%2FIlxsf2ZdNmZ55q8yF70GS88vrXHgoQ%2FR97rMgU7gzO23RR6oskWl5HFjCuJt3bHC8662qIbsBGqZDII1aKmOykwVjKd3juUDx2%2Fwfu%2BYNKU8kuUJ&X-Amz-Signature=a17041192e92e393b25a53ddf33299e7f848b97ea45f9c604861191e6ea0053a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







