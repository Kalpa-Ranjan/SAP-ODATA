



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4PNDI3Y%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T190944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDdM9Jt4O%2F2SVbV8cxwZmdik3abP15Mph3IeHCp2CMN3wIgFLEc8yk84ud9GBnhvbMacBgFY4770EVdewez27ywa68qiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN5Ug4Ivu5ktg0JP8CrcA6Hu4yM%2FY8k1NXr7IfyZ%2F1cJrk%2Bqu9KOFyuWfoaA%2FwluVogteecb%2BHWSEJVi9O1DlDQRDGCxMTKutyNSDx6WLrZ%2FRMiM6YI%2BgOjyM6UkBTZ4j53%2FwbIrGgLqslkAXWRMMr1o5MGax6v4sqnxZeZpjSJpDMkACi2EE%2FntH6481o8hq3G6YTXqRZWTZv%2B%2BwKwPYm9LQcgdAjciVbyE5Yek2tJo4sA9fgP9NCcdD96HTYx8o9LuutcAY%2Bv1lb%2FUqSiCjl7S9d7v5zrrsTXyuiAcgP9Bt4qpnHNjasxUiRUJS0lS00dqrq%2BpzmPFHS1D7bFgo0VKiQ6fMRBp%2BGaCR9JttRRh4F9Q8Xl2U8QtLPA8wzsDAjfVATHuW1lel2nMSy07viRwRvjnyLuA3leN0mOSabN4I1IX%2BOWb8jey1rJTjyYlMPwPsBWTQxW5GopODext5Z3vy6uvdwYzGE39sEWZ%2F5pOnKaSiIZciQCMkvmZuO00Zzq0%2FEVwz2C%2FiuIWrfFTPVdaNlMD16Aln7Qy%2FjtjJaqYQVvV%2F%2BVAjsiQllgqKWMlXKZI7qKQ1Q2Z8sR0SFLztIuVbEpc2Ui8yHnkKugxqGPjW7u7q0TqdjHBnF4dvKnp6qL56k9Heqf8HRCXML%2FB%2BM8GOqUB7gNjdcI3Ziey6Q9Q2dlx84opSPBfvdGY5llhPKvW1QwEkGBTF3LyuuGiGPO8Lak4dWizui9PnLdZfbgfTWP89uPVYTSPwg%2F4P7JuPW9Lmf3zVwyGUPyIHLtWyPjE9gDD2tR%2B%2FZc7kN%2FxXSanD5Ge05dpglkTgGiOktZs5dpCc%2FP4jWKUFbq7gm20dou0ElcSWAwcVQJfeJ6ri%2Fstg7rMXuhii61o&X-Amz-Signature=b6295a9f54f49ebf9e56b19fd50aae1d47ce045fde93a9851392a9a0a91ca831&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4PNDI3Y%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T190944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDdM9Jt4O%2F2SVbV8cxwZmdik3abP15Mph3IeHCp2CMN3wIgFLEc8yk84ud9GBnhvbMacBgFY4770EVdewez27ywa68qiAQI0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN5Ug4Ivu5ktg0JP8CrcA6Hu4yM%2FY8k1NXr7IfyZ%2F1cJrk%2Bqu9KOFyuWfoaA%2FwluVogteecb%2BHWSEJVi9O1DlDQRDGCxMTKutyNSDx6WLrZ%2FRMiM6YI%2BgOjyM6UkBTZ4j53%2FwbIrGgLqslkAXWRMMr1o5MGax6v4sqnxZeZpjSJpDMkACi2EE%2FntH6481o8hq3G6YTXqRZWTZv%2B%2BwKwPYm9LQcgdAjciVbyE5Yek2tJo4sA9fgP9NCcdD96HTYx8o9LuutcAY%2Bv1lb%2FUqSiCjl7S9d7v5zrrsTXyuiAcgP9Bt4qpnHNjasxUiRUJS0lS00dqrq%2BpzmPFHS1D7bFgo0VKiQ6fMRBp%2BGaCR9JttRRh4F9Q8Xl2U8QtLPA8wzsDAjfVATHuW1lel2nMSy07viRwRvjnyLuA3leN0mOSabN4I1IX%2BOWb8jey1rJTjyYlMPwPsBWTQxW5GopODext5Z3vy6uvdwYzGE39sEWZ%2F5pOnKaSiIZciQCMkvmZuO00Zzq0%2FEVwz2C%2FiuIWrfFTPVdaNlMD16Aln7Qy%2FjtjJaqYQVvV%2F%2BVAjsiQllgqKWMlXKZI7qKQ1Q2Z8sR0SFLztIuVbEpc2Ui8yHnkKugxqGPjW7u7q0TqdjHBnF4dvKnp6qL56k9Heqf8HRCXML%2FB%2BM8GOqUB7gNjdcI3Ziey6Q9Q2dlx84opSPBfvdGY5llhPKvW1QwEkGBTF3LyuuGiGPO8Lak4dWizui9PnLdZfbgfTWP89uPVYTSPwg%2F4P7JuPW9Lmf3zVwyGUPyIHLtWyPjE9gDD2tR%2B%2FZc7kN%2FxXSanD5Ge05dpglkTgGiOktZs5dpCc%2FP4jWKUFbq7gm20dou0ElcSWAwcVQJfeJ6ri%2Fstg7rMXuhii61o&X-Amz-Signature=34be1cc5ea40bc811508f833ef88ca662f10e4afb6995df3ee42f7b5da00b198&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







