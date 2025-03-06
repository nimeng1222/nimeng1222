def a(mo):
    if isinstance(mo,(int,float)):
        if 50 <= mo <= 100:
            b = 0.1
        elif mo > 100:
            b = 0.2
        else:
            b  = 0
        c = (1-b)*mo
        return (f"我的折扣是：{b}" "\n"
                f"我最终要付的价格是：{c:.2f}")
    else:
        return "请输入正确的数字!"


print(a(22.22))

