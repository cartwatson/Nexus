import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Layout, Menu } from 'antd';
import { HomeOutlined, FileImageOutlined, AimOutlined, CameraOutlined } from '@ant-design/icons';

const { Header } = Layout;

const HeaderComponent: React.FC = () => {
    const location = useLocation();
    const [selectedKey, setSelectedKey] = useState<string>(() => {
        // Get the initial selected key based on the current page URL
        const path = location.pathname;
        switch (path) {
            case '/':
                return '1';
            case '/satellites':
                return '2';
            case '/droids':
                return '3';
            case '/images':
                return '4';
            default:
                return '';
        }
    });

    useEffect(() => {
        const path = location.pathname;
        switch (path) {
            case '/':
                setSelectedKey('1');
                break;
            case '/satellites':
                setSelectedKey('2');
                break;
            case '/droids':
                setSelectedKey('3');
                break;
            case '/images':
                setSelectedKey('4');
                break;
            default:
                setSelectedKey('');
        }
    }, [location.pathname]);

    return (
        <Header style={{padding: '0'}}>
            <div className="logo" />
            <Menu theme="dark" mode="horizontal" defaultSelectedKeys={[selectedKey]}>
                <Menu.Item key="1" icon={<HomeOutlined />}>
                    <Link to="/">Nexus</Link>
                </Menu.Item>
                <Menu.Item key="2" icon={<AimOutlined />}>
                    <Link to="/satellites">Satellites</Link>
                </Menu.Item>
                <Menu.Item key="3" icon={<CameraOutlined />}>
                    <Link to="/droids">Droids</Link>
                </Menu.Item>
                <Menu.Item key="4" icon={<FileImageOutlined />}>
                    <Link to="/images">Images</Link>
                </Menu.Item>
            </Menu>
        </Header>
    );
};

export default HeaderComponent;

