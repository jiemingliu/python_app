# 利用库selenium模拟鼠标键盘操作实现自动化  
1. 读excel用xlrd  
2. 写excel用xlwt  
  
## selenium一些用法
1. 选择元素，一般有by_id,by_name,by_class等，这些都很好理解，此处说明的是by_css_selector  
1.1 根据tagName，driver.find_element_by_css_selector("input")
1.2 根据ID，"#IDName" 或者 "input#IDName"
1.3 根据className，".className" 或者 ".className1.className2.className3"
1.4 根据元素属性，"input[name=userName]" 或者 "img[alt]" 或者多个属性混合

## tips:自动验证码识别正确率太低，故手动输入验证到VerificationCode.txt中