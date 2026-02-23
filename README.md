



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JWIABAG%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T185616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIDw5QfkVLc0HvsCmsY5DieAdC%2BJiCk1godeNcISoyin2AiEAmvRYNenviBSGbPWm3nHNHeBIcLZOU6D8BKnuLqyHNngqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN0np8eraR%2BzZI%2Fz3yrcA9lYSV5UHrTfdo%2FomOmxD4QQBMwaILeYc045dbt0E1aLNRfHAui1Msz1k%2BzWk%2FGDgUP0iaZSk977yrBvwNoa02dbBiCKL1%2BR1GXGHo4k6l%2BE%2Fm63BoY%2BBRwI1goSKE%2BnZh08I4OcgkplrkFYaq%2Brr8eDV0yMhSI%2FlvSjtf0hCIJCsW0%2BtyA9LDiq8aNaSgP30SRfqDrqBcEBc02spBuOcjHdCClLbJ1YiUkijAjkR%2B73qz5C8gJqZq7Q%2BwJt7WPHHt%2Bcl1whEfWE2ATppPni4qc2Nzi00L2opv2hXNMwLCf3%2Bd2Qua%2FYyIcpTqYWiUJO6IQttSXv9v0jCRkLVj5%2Ft%2BaFJSLvloIvoE0Qug5ZXSAHm%2BtwKjM5fgStRW5fgjY8RxKvX6Ss%2FH8uW4gCqWiFcd84eBt3E%2FONgJZAVpUmmWLyLU%2FBRP%2BvEP2Wu5hxSV59jR%2FngyiGMU6WHz%2BTtcVc0lbLO9zVXywpS%2FqItU9EmOG6M6Cku3hfm4ob6LaL%2B4DL8Sp7DGP3i9AkWV5yNBz2N5O7HDmSc9E5SXenpiGrN3e3nERJAyTknqc%2BFKRGK8vhjMPHbcn%2FeMNFA%2Byw7Sge%2FNovFBB6ipJl%2FSTegnj1bE6rzh%2BpeBHcfjkndx0TMLau8swGOqUB31T72mv5DqV%2BDR%2BVOY6H18iqR4u2iKrKzi5ELYFCNqxfNkGVdm8XJMX2movbOFW8HSXYpUtumjl6lwugR2OSRZD81VDDBG%2BhD1kKqbtAfZEVLtD%2FJbzmHOk373lkzPDTwzGNRvdqEIw7U2t8sDcHrp30ZJXZkm%2BzfPs3cKdLWQmJ7pHSBQgtXBnNR%2FpzqQscpp9nberogCzCe0NlzUMckYXHexc7&X-Amz-Signature=a7cbe7119c9e4e4669b235db9f678b761b4383eb2c79bc6d79c344aca33defe5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JWIABAG%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T185616Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIDw5QfkVLc0HvsCmsY5DieAdC%2BJiCk1godeNcISoyin2AiEAmvRYNenviBSGbPWm3nHNHeBIcLZOU6D8BKnuLqyHNngqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN0np8eraR%2BzZI%2Fz3yrcA9lYSV5UHrTfdo%2FomOmxD4QQBMwaILeYc045dbt0E1aLNRfHAui1Msz1k%2BzWk%2FGDgUP0iaZSk977yrBvwNoa02dbBiCKL1%2BR1GXGHo4k6l%2BE%2Fm63BoY%2BBRwI1goSKE%2BnZh08I4OcgkplrkFYaq%2Brr8eDV0yMhSI%2FlvSjtf0hCIJCsW0%2BtyA9LDiq8aNaSgP30SRfqDrqBcEBc02spBuOcjHdCClLbJ1YiUkijAjkR%2B73qz5C8gJqZq7Q%2BwJt7WPHHt%2Bcl1whEfWE2ATppPni4qc2Nzi00L2opv2hXNMwLCf3%2Bd2Qua%2FYyIcpTqYWiUJO6IQttSXv9v0jCRkLVj5%2Ft%2BaFJSLvloIvoE0Qug5ZXSAHm%2BtwKjM5fgStRW5fgjY8RxKvX6Ss%2FH8uW4gCqWiFcd84eBt3E%2FONgJZAVpUmmWLyLU%2FBRP%2BvEP2Wu5hxSV59jR%2FngyiGMU6WHz%2BTtcVc0lbLO9zVXywpS%2FqItU9EmOG6M6Cku3hfm4ob6LaL%2B4DL8Sp7DGP3i9AkWV5yNBz2N5O7HDmSc9E5SXenpiGrN3e3nERJAyTknqc%2BFKRGK8vhjMPHbcn%2FeMNFA%2Byw7Sge%2FNovFBB6ipJl%2FSTegnj1bE6rzh%2BpeBHcfjkndx0TMLau8swGOqUB31T72mv5DqV%2BDR%2BVOY6H18iqR4u2iKrKzi5ELYFCNqxfNkGVdm8XJMX2movbOFW8HSXYpUtumjl6lwugR2OSRZD81VDDBG%2BhD1kKqbtAfZEVLtD%2FJbzmHOk373lkzPDTwzGNRvdqEIw7U2t8sDcHrp30ZJXZkm%2BzfPs3cKdLWQmJ7pHSBQgtXBnNR%2FpzqQscpp9nberogCzCe0NlzUMckYXHexc7&X-Amz-Signature=00b8f06ad6147ab0e50b65a47b87ba29fc61b7314086dea7cc20ce004747f265&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







