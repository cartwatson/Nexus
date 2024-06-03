import React from 'react';
import { Layout } from 'antd';
import { LinkedinOutlined, GithubOutlined } from '@ant-design/icons';

const { Footer } = Layout;

const FooterComponent: React.FC = () => {
    return (
        <Footer>
          <div>© 2024 Carter Watson <a href="https://github.com/cartwatson"><GithubOutlined /></a></div>
        </Footer >
    );
};

export default FooterComponent;

