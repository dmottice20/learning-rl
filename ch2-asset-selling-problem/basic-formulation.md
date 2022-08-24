# Asset Selling Problem

| Problem Type | Chapter.Section | Page # |
| ----------- | ----------- | ----------- |
| Standard      | 2.2       | 33 |

*[Warren Powell's Sequential Decision Analytics](https://castlelab.princeton.edu/wp-content/uploads/2022/01/Powell-Sequential-Decision-Analytics-Jan292022-2.pdf)*

## Narrative

XYZ Investment Services is a family investment firm. They have asked us to help determine when to sell a single share of stock.
Assume we are holding a block of shares for a certain stock. If we sell at time $t$, we earn that price. This price varies according to some random process over time. Once the shares of stock are sold, the process stops.

## Basic Formulation

#### State Variables

Let $R_t$ be the physical state variable at time $t$, given by
$$
R_t=\begin{cases}
    1 &, \text{ if holding the stock at time $t$}\\
    0 &, \text{ if no longer holding the stock at time $t$}
\end{cases}.
$$

Let $S_t$ be the state of the system at time $t$ given by $$S_t=(R_t, p_t)$$ where $p_t$ is the price per share at time $t$.

#### Decision Variables

At each time step $t$, we have a choice to hold or sell the stock. Let $x_t$ be this action given by 
$$
x_t=\begin{cases}
    1&,\text{ if selling at time $t$}\\
    0&,\text{ if holding at time $t$}
\end{cases}
$$

We can only sell if we are holding the stock; therefore, we have a constraint $$x_t\leq R_t.$$

#### Exogenous Information

The random process for $p_t$ is the only source of uncertainty in our system, given by $$W_{t+1}=(\hat{p}_{t+1}).$$

#### Transition Function

Let $S^M$ be the system model for this process, given by $$S_{t+1}=S^M(S_t, X^\pi(S_t), W_{t+1})$$ where $X^\pi(S_t)$ is the policy. 

#### Objective Function

The contribution function is given by $$C(S_t, x_t)=p_t x_t$$ as we will not receive the money from our investment until we sell it.
