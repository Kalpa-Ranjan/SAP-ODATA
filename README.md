



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SQQGXLC%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T012454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxKL5KhhsVKkDAbLjfaRIzB%2Fa9GpgbOu0OIAE1iakv6gIgHcJnXHyfRri1BncXZs42I3iuIG8WEJIsOtQ4vt%2FmIpIqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL5Yo57wy9IuKFB7tircAw8uLfK9wsFdBsr%2B0OxDuXqft1aHARdo7oc%2FFggyV7hp2ip%2FuNhObQuvbfmAhI%2BTdh8Mf07qS0SCQdhRb0rJEGpf92Q9Hw26cFoFPHJWWSfCsC4f8qSHdt9bPZVv5dQo5mgOwkzxq88eitb5LViahs6XX42t%2FGjUg7aOp7rggU5NGGTMftpRMx4UpOVfs27xWwWs8DxZPKuxHEWPm9DxC3LfNv%2FNZp4K4a0PwZaru8LotRMLUuONByGRlvEc9GOStbbrm3uLQ80Xaa2bT5fOhAgXydIZ3bZDk3VMkiBKYTh%2BOtxFS5sNi2oA9qLsPn8iXAesMg3HhkFSJKNeEMU%2FF98UcfTA5ag56QscUi3%2BZc3ZnfBlMqnOpdRh24V7zLBdqeC4KZP1mN4Ebunnzx9pHEvot13rNiE0SY2GGkPIxesL5xOvuN7dX94DqP3%2FC60XpJQPvabPEExBpwwU6rlTPJUria%2BXXvRTrbMDaDwLU9P38wwSloxPUmm7PAz6qplJa%2BCadakDFVi1AEebWKIu301k2bksqfo4j%2FV0Yb%2FJiBepM6Nabt0pXwU3y9%2FLlmlza8cFh7L1gmul416HG35zoZUvNUecROYQfzqIabVmCaAw3DVeCBjPkcYQytqOMLL21coGOqUBcpoU6pPE99OiPAFuhFvxjzkj%2F2u7%2FxCJOSpvmWOojH3naxZhU6%2B8Dvt19YaCvQxhD6F5V73EMR4ueEUFWTB5dRd01q5uu%2FohMEA5TlcDTWa9xab77wmnQznhA65tCTxRRqBxFimTYjlJ4XFjZoiKUnnd0ANlHajzjhFJ8Q7s5jeIyPiZRRTA31C051lkSkEIjdMk0wTo9Oajvd3i%2BVB1DggKWiNw&X-Amz-Signature=d75b9c9011722a2d06c225dcb0b6940f36be53125fe8524ecbb26d6cc94c01c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SQQGXLC%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T012454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQDxKL5KhhsVKkDAbLjfaRIzB%2Fa9GpgbOu0OIAE1iakv6gIgHcJnXHyfRri1BncXZs42I3iuIG8WEJIsOtQ4vt%2FmIpIqiAQI1f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL5Yo57wy9IuKFB7tircAw8uLfK9wsFdBsr%2B0OxDuXqft1aHARdo7oc%2FFggyV7hp2ip%2FuNhObQuvbfmAhI%2BTdh8Mf07qS0SCQdhRb0rJEGpf92Q9Hw26cFoFPHJWWSfCsC4f8qSHdt9bPZVv5dQo5mgOwkzxq88eitb5LViahs6XX42t%2FGjUg7aOp7rggU5NGGTMftpRMx4UpOVfs27xWwWs8DxZPKuxHEWPm9DxC3LfNv%2FNZp4K4a0PwZaru8LotRMLUuONByGRlvEc9GOStbbrm3uLQ80Xaa2bT5fOhAgXydIZ3bZDk3VMkiBKYTh%2BOtxFS5sNi2oA9qLsPn8iXAesMg3HhkFSJKNeEMU%2FF98UcfTA5ag56QscUi3%2BZc3ZnfBlMqnOpdRh24V7zLBdqeC4KZP1mN4Ebunnzx9pHEvot13rNiE0SY2GGkPIxesL5xOvuN7dX94DqP3%2FC60XpJQPvabPEExBpwwU6rlTPJUria%2BXXvRTrbMDaDwLU9P38wwSloxPUmm7PAz6qplJa%2BCadakDFVi1AEebWKIu301k2bksqfo4j%2FV0Yb%2FJiBepM6Nabt0pXwU3y9%2FLlmlza8cFh7L1gmul416HG35zoZUvNUecROYQfzqIabVmCaAw3DVeCBjPkcYQytqOMLL21coGOqUBcpoU6pPE99OiPAFuhFvxjzkj%2F2u7%2FxCJOSpvmWOojH3naxZhU6%2B8Dvt19YaCvQxhD6F5V73EMR4ueEUFWTB5dRd01q5uu%2FohMEA5TlcDTWa9xab77wmnQznhA65tCTxRRqBxFimTYjlJ4XFjZoiKUnnd0ANlHajzjhFJ8Q7s5jeIyPiZRRTA31C051lkSkEIjdMk0wTo9Oajvd3i%2BVB1DggKWiNw&X-Amz-Signature=aac39e98839985928d73288af2b3c623cb0f147b2a5e5c5b1d0b50cb1d7fecdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







