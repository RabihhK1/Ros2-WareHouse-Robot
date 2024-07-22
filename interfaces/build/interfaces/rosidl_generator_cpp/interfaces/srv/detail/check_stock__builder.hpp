// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from interfaces:srv/CheckStock.idl
// generated code does not contain a copyright notice

#ifndef INTERFACES__SRV__DETAIL__CHECK_STOCK__BUILDER_HPP_
#define INTERFACES__SRV__DETAIL__CHECK_STOCK__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "interfaces/srv/detail/check_stock__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_CheckStock_Request_item_name
{
public:
  Init_CheckStock_Request_item_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::CheckStock_Request item_name(::interfaces::srv::CheckStock_Request::_item_name_type arg)
  {
    msg_.item_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::CheckStock_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::CheckStock_Request>()
{
  return interfaces::srv::builder::Init_CheckStock_Request_item_name();
}

}  // namespace interfaces


namespace interfaces
{

namespace srv
{

namespace builder
{

class Init_CheckStock_Response_stock_level
{
public:
  Init_CheckStock_Response_stock_level()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::interfaces::srv::CheckStock_Response stock_level(::interfaces::srv::CheckStock_Response::_stock_level_type arg)
  {
    msg_.stock_level = std::move(arg);
    return std::move(msg_);
  }

private:
  ::interfaces::srv::CheckStock_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::interfaces::srv::CheckStock_Response>()
{
  return interfaces::srv::builder::Init_CheckStock_Response_stock_level();
}

}  // namespace interfaces

#endif  // INTERFACES__SRV__DETAIL__CHECK_STOCK__BUILDER_HPP_
