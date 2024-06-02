import React from 'react';
import { Layout, Menu } from 'antd';
import { FileImageOutlined, AimOutlined, CameraOutlined } from '@ant-design/icons';
// import './Header.css';

const { Header } = Layout;

const HeaderComponent: React.FC = () => {
    return (
        <Header>
            <div className="logo" />
            <Menu theme="dark" mode="horizontal">
                <Menu.Item key="1" icon={<AimOutlined />}>Satellites</Menu.Item>
                <Menu.Item key="2" icon={<CameraOutlined />}>Droids</Menu.Item>
                <Menu.Item key="3" icon={<FileImageOutlined />}>Images</Menu.Item>
            </Menu>
            <ul>
                <li><a href='/satellites'>Satellites</a></li>
                <li><a href='/droids'>Droids</a></li>
                <li><a href='/images'>Images</a></li>
            </ul>
        </Header>
    );
};

export default HeaderComponent;

